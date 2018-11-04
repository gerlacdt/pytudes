from collections import defaultdict, deque


def toInt(val, regs):
    try:
        v = int(val)
        return v
    except ValueError:
        return regs[val]


def duet(input1):
    ops = tuple([line.split() for line in input1.splitlines()])
    registers = defaultdict(int)
    pc = snd = 0

    while True:
        op = ops[pc]
        o, x, y = op[0], op[1], op[-1]
        vy = toInt(y, registers)
        if o == 'snd': snd = registers[x]
        elif o == 'set': registers[x] = vy
        elif o == 'add': registers[x] += vy
        elif o == 'mul': registers[x] *= vy
        elif o == 'mod': registers[x] %= vy
        elif o == 'jgz' and registers[x] > 0: pc += vy - 1
        elif o == 'rcv' and registers[x] != 0: return snd
        pc += 1


def deadlock(input1):
    # read input
    ops = tuple([line.split() for line in input1.splitlines()])

    # init programs
    registers0 = defaultdict(int, p=0)
    pc0 = 0
    q0 = deque([])
    q1 = deque([])
    num_of_snds = 0
    # program consists of operations, registers, current pc, the queue,
    # number of sended messages and the other proram's queue, progress
    program0 = (ops, registers0, pc0, q0, num_of_snds, q1, False)
    registers1 = defaultdict(int, p=1)
    pc1 = 0
    program1 = (ops, registers1, pc1, q1, num_of_snds, q0, False)

    while True:
        program0 = run(program0)
        program1 = run(program1)
        if not program0[6] and not program1[6]:   # check progress of programs
            break

    return program1[4]  # return number_of_snds


def run(program):
    ops, registers, pc, q, num_of_snds, otherq, _ = program
    progress = False
    while True:
        op = ops[pc]
        o, x, y = op[0], op[1], op[-1]
        if o == 'rcv' and not q:
            break
        vy = toInt(y, registers)
        if o == 'snd':
            y = toInt(x, registers)
            num_of_snds += 1
            otherq.append(y)
        elif o == 'set': registers[x] = vy
        elif o == 'add': registers[x] += vy
        elif o == 'mul': registers[x] *= vy
        elif o == 'mod': registers[x] %=  vy
        elif o == 'jgz':
            if toInt(x, registers) > 0:
                pc += toInt(y, registers) -1
        elif o == 'rcv':
            y = q.popleft()
            registers[x] = toInt(y, registers)
        pc += 1
        progress = True

    return (ops, registers, pc, q, num_of_snds, otherq, progress)
