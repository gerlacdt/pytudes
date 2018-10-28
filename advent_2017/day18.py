from collections import defaultdict, deque

input1 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""


def duet(input1):
    ops = tuple([line.split() for line in input1.splitlines()])
    registers = defaultdict(int)
    sound = ('', 0)
    pc = 0

    def toInt(val):
        try:
            v = int(val)
            return v
        except ValueError:
            return registers[val]

    def regset(op):
        _, reg, val = op
        registers[reg] = toInt(val)

    def regadd(op):
        _, reg, val = op
        registers[reg] += toInt(val)

    def regmul(op):
        _, reg, val = op
        registers[reg] *= toInt(val)

    def regmod(op):
        _, reg, val = op
        registers[reg] %= toInt(val)

    def regsnd(op):
        o, reg = op
        nonlocal sound
        sound = (reg, registers[reg])

    def regrcv(op):
        o, reg = op
        if registers[reg] != 0:
            return True

    def regjgz(op):
        o, reg, val = op
        nonlocal pc
        if toInt(reg) > 0:
            pc += toInt(val)

    def execute(op):
        "op is a triple (op, register, number)"
        operations = {
            'set': regset,
            'add': regadd,
            'mul': regmul,
            'mod': regmod,
            'snd': regsnd,
            'rcv': regrcv,
            'jgz': regjgz,
        }
        return operations[op[0]](op)

    while True:
        op = ops[pc]
        oldpc = pc
        result = execute(op)
        if result is True:
            break

        # only increment pc if it was not change in the executed operation, e.g. jump
        if oldpc == pc:
            pc += 1

    return sound


input2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
"""


def deadlock(input1):
    # read input
    ops = tuple([line.split() for line in input1.splitlines()])

    # init programs
    registers0 = defaultdict(int)
    registers0['p'] = 0
    pc0 = 0
    q0 = deque([])
    q1 = deque([])
    num_of_snds = 0
    # program consists of operations, registers, current pc, the queue,
    # number of sended messages and the other proram's queue, progress
    program0 = (ops, registers0, pc0, q0, num_of_snds, q1, False)
    registers1 = defaultdict(int)
    registers1['p'] = 1
    pc1 = 0
    program1 = (ops, registers1, pc1, q1, num_of_snds, q0, False)

    while True:
        program0 = run(program0)
        program1 = run(program1)
        if not program0[6] and not program1[6]:
            break

    return (program0[4], program1[4])  # return number_of_snds


def run(program):
    ops, registers, pc, q, num_of_snds, otherq, _ = program

    def toInt(val):
        try:
            v = int(val)
            return v
        except ValueError:
            return registers[val]

    def regsnd(op):
        o, reg = op
        val = toInt(reg)
        nonlocal num_of_snds
        num_of_snds += 1
        otherq.append(val)

    def regrcv(op):
        _, reg = op
        val = q.popleft()
        registers[reg] = toInt(val)

    def regset(op):
        _, reg, val = op
        registers[reg] = toInt(val)

    def regadd(op):
        _, reg, val = op
        registers[reg] += toInt(val)

    def regmul(op):
        _, reg, val = op
        registers[reg] *= toInt(val)

    def regmod(op):
        _, reg, val = op
        registers[reg] %= toInt(val)

    def execute(op):
        "op is a triple (op, register, number)"
        operations = {
            'set': regset,
            'add': regadd,
            'mul': regmul,
            'mod': regmod,
            'snd': regsnd,
            'rcv': regrcv,
            'jgz': regjgz,
        }
        return operations[op[0]](op)

    def regjgz(op):
        o, reg, val = op
        nonlocal pc
        if toInt(reg) > 0:
            pc += toInt(val)

    progress = False
    while True:
        op = ops[pc]
        if op[0] == 'rcv' and not q:
            break
        oldpc = pc
        execute(op)
        progress = True
        # only increment pc if it was not change in the executed operation, e.g. jump
        if oldpc == pc:
            pc += 1

    return (ops, registers, pc, q, num_of_snds, otherq, progress)
