import utils


def getInput():
    return utils.Inputstr("08")


def parse(text):
    return [(line.split()[0], int(line.split()[1])) for line in text.splitlines()]


def handheld(instructions):
    acc = 0
    pc = 0
    visited = set()

    while True:
        if pc == len(instructions):
            break
        if pc in visited:
            return acc, False
        visited.add(pc)
        if pc < 0 or pc >= len(instructions):
            return acc, False
        op, val = instructions[pc]
        if op == "nop":
            pc += 1
        elif op == "acc":
            acc += val
            pc += 1
        elif op == "jmp":
            pc += val
        else:
            raise RuntimeError(f"Error, invalid instructions {op}")

    return acc, True


def fix(instructions):
    for i, instr in enumerate(instructions):
        copy = instructions[:]
        op, val = instr
        if op == "nop":
            copy[i] = ("jmp", val)
        elif op == "jmp":
            copy[i] = ("nop", val)
        else:
            continue
        acc, correct = handheld(copy)
        if correct:
            return acc
    return None


def testExample():
    text = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

    instructions = parse(text)
    actual, _ = handheld(instructions)
    expected = 5
    assert actual == expected


def testExample2():
    text = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

    instructions = parse(text)
    actual = fix(instructions)
    expected = 8
    assert actual == expected


def testPart1():
    actual, _ = handheld(parse(getInput()))
    expected = 1134
    assert actual == expected


def testPart2():
    actual = fix(parse(getInput()))
    expected = 0
    assert actual == expected
