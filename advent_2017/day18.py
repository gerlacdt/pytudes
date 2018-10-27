from collections import defaultdict

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
            pc += int(val)

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
