from collections import defaultdict
from utils import Array, operations


def part12(s):
    lines = s.splitlines()
    instructions = Array(lines)
    registers = defaultdict(int)

    highest = 0
    for (r, inc, delta, _if, r2, cmp, amount) in instructions:
        if operations[cmp](registers[r2], amount):
            registers[r] += delta * (+1 if inc == 'inc' else -1)
        currentMax = max(registers.values())
        highest = currentMax if highest < currentMax else highest

    return max(registers.values()), highest
