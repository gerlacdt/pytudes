import utils

from collections import defaultdict, namedtuple


def getInput():
    line = utils.Inputstr("06")
    return utils.Vector(line)


def laternfish(fishes, days):

    table = [0 for _ in range(9)]
    for val in fishes:
        table[val] += 1

    for i in range(days):
        current = [0 for _ in range(9)]
        for timer in range(0, 9):
            if timer == 0:
                current[8] += table[0]
                current[6] += table[0]
            else:
                current[timer - 1] += table[timer]
        table = current
    return sum(table)


Case = namedtuple("Case", ["fishes", "days", "expected"])

example = "3,4,3,1,2"


def test_laternfish_example():
    fishes = utils.Vector(example)
    cases = [
        Case(fishes, 18, 26),
        Case(fishes, 80, 5934),
        Case(fishes, 256, 26984457539),
    ]

    for c in cases:
        actual = laternfish(c.fishes, c.days)

        assert actual == c.expected


def test_laternfish():
    fishes = getInput()

    cases = [Case(fishes, 80, 343441), Case(fishes, 256, 1569108373832)]
    for c in cases:
        actual = laternfish(c.fishes, c.days)
        assert actual == c.expected
