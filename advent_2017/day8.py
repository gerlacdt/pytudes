input1 = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''


def parse(s):
    lines = s.splitlines()
    data = [line.split() for line in lines]
    return data


def isTrue(registers, condition):
    register, operator, value = condition

    opTable = {'>': registers[register] > int(value),
               '>=': registers[register] >= int(value),
               '<': registers[register] < int(value),
               '<=': registers[register] <= int(value),
               '==': registers[register] == int(value),
               '!=': registers[register] != int(value)}

    return opTable[operator]


def execute(registers, instr):
    register, instr, value, _, *condition = instr
    if instr == 'inc':
        if isTrue(registers, condition):
            registers[register] += int(value)
    elif instr == 'dec':
        if isTrue(registers, condition):
            registers[register] -= int(value)
    return None


def part12(s):
    instructions = parse(s)
    registers = {instr[0]: 0 for instr in instructions}

    allTimeMax = 0
    for instr in instructions:
        execute(registers, instr)
        currentMax = max(registers.values())
        allTimeMax = currentMax if allTimeMax < currentMax else allTimeMax

    return max(registers.values()), allTimeMax
