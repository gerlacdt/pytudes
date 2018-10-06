from myutils import readFile


def readInstructions(content):
    lines = content.splitlines()
    return [int(x) for x in lines]


def maze(instructions):
    current = 0
    maxLength = len(instructions)
    steps = 0
    while current < maxLength:
        instr = instructions[current]
        instructions[current] += 1  # increment instructions
        current += instr  # move
        steps += 1

    return steps


def maze2(instructions):
    current = 0
    maxLength = len(instructions)
    steps = 0
    while current < maxLength or current <= 0:
        instr = instructions[current]
        if instr >= 3:
            instructions[current] -= 1
        else:
            instructions[current] += 1  # increment instructions
        current += instr  # move
        steps += 1
    return steps
