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
    opcode = code[0]
    i = 0
    if replace:
        code[1] = 12
        code[2] = 2
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


def test():
    actual = part1(list(getInput()))
    expected = 5866714
    assert actual == expected


def testSimple():
    actual = part1([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], False)
    expected = 3500
    assert actual == expected

    actual = part1([1, 1, 1, 4, 99, 5, 6, 0, 99], False)
    expected = 30
    assert actual == expected
