import utils


def getInput():
    return utils.Vector(utils.Inputstr("02"))


# 1 addition
# 2 multiply
# 99 halt
# unknown error
OPCODES = set([1, 2, 99])
STEP = 4


def execute(code, opcode, op1, op2):
    if opcode == 1:
        return code[op1] + code[op2]
    elif opcode == 2:
        return code[op1] * code[op2]
    raise RuntimeError("Wrong opcode: {}".format(opcode))


def part1(code, replace=True):
    return run(code[:], (12, 2))


def run(code, pair):
    opcode = code[0]
    i = 0
    code[1] = pair[0]
    code[2] = pair[1]
    while True:
        opcode = code[i]
        if opcode not in OPCODES:
            raise RuntimeError("Wrong opcode: {}".format(opcode))
        elif opcode == 99:
            break
        op1, op2, rs = code[i + 1], code[i + 2], code[i + 3]
        result = execute(code, opcode, op1, op2)
        code[rs] = result
        i += STEP
    return code[0]  # result is the first number in programm


def part2(code, output=19690720):
    for i in range(100):
        for j in range(100):
            if output == run(code[:], (i, j)):
                return (i, j)
    return None


def test():
    actual = part1(list(getInput()))
    expected = 5866714
    assert actual == expected


def testPart2():
    actual = part2(list(getInput()))
    expected = (52, 8)
    assert actual == expected
    noun, verb = actual
    assert (100 * noun) + verb == 5208
