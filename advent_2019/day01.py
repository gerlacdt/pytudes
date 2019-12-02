import utils

from collections import namedtuple


def getInput():
    return utils.Integers(utils.Inputstr("01"))


def calcFuelComplex(n):
    current = n
    result = 0
    while True:
        current = (current // 3) - 2
        if current < 0:
            return result
        result += current


def calcFuelSimple(n):
    return (n // 3) - 2


def fuel(calc=calcFuelSimple):
    fuelCounts = getInput()
    return sum([calc(n) for n in fuelCounts])


def test():
    actual = fuel()
    expected = 3342351
    assert actual == expected


def testPart2():
    actual = fuel(calcFuelComplex)
    expected = 5010664
    assert actual == expected


def testCalcComplex():
    Case = namedtuple("Case", ["n", "expected"])
    cases = [Case(14, 2), Case(1969, 966)]
    for c in cases:
        actual = calcFuelComplex(c.n)
        assert actual == c.expected
