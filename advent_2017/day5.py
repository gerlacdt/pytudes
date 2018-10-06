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
    while 0 <= current < maxLength:
        instr = instructions[current]
        instructions[current] += (-1 if instructions[current] >= 3 else 1)
        current += instr  # move
        steps += 1
    return steps
