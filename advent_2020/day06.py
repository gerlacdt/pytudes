import utils
from functools import reduce


def getInput():
    return utils.Inputstr("06").splitlines()


LINES = getInput()


def customs(lines=LINES, fn=lambda x, y: x.union(y)):
    groups = []
    current = []
    for line in lines:
        if line == "":
            groups.append(current)
            current = []
        else:
            current.append(frozenset(line))
    groups.append(current)
    return sum([len(item) for item in [reduce(fn, g) for g in groups]])


def test():
    lines = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
    actual = customs(lines.splitlines())
    expected = 11
    assert actual == expected


def testPart1():
    actual = customs()
    expected = 6382
    assert actual == expected


def testPart2():
    actual = customs(LINES, lambda x, y: x.intersection(y))
    expected = 3197
    assert actual == expected
