from numba import jit
from myutils import readFile


def toInt(val, regs):
    try:
        v = int(val)
        return v
    except ValueError:
        return regs[val]


INPUT1 = readFile('./data/input23.txt')


def conflagration(input1):
    program = tuple([line.split() for line in input1.splitlines()])
    registers = {L: 0 for L in "abcdefgh"}
    mulcount = pc = 0

    while pc >= 0 and pc < len(program):
        op, x, y = program[pc]
        pc += 1
        vy = toInt(y, registers)
        vx = toInt(x, registers)
        if op == 'set': registers[x] = vy
        elif op == 'sub': registers[x] -= vy
        elif op == 'mul': registers[x] *= vy; mulcount += 1
        elif op == 'jnz' and vx: pc += vy - 1

    return mulcount


assert(conflagration(INPUT1) == 3025)


@jit
def debug():
    a = 1
    d = e = f = g = h = 0
    b = 57
    c = b
    if a:
        b *= 100
        b -= -100000
        c = b
        c -= -17000
    while True:
        f = 1
        d = 2
        e = 2
        while True:
            if b % d == 0:
                f = 0
            d -= -1
            g = d - b
            if g == 0:
                if f == 0:
                    h -= -1
                g = b - c
                if g == 0:
                    return h
                b -= -17
                break


assert(debug() == 915)
