import utils


def getInput():
    lines = utils.Inputstr("07")
    return utils.Vector(lines)


def fuel(positions):
    result = float("inf")
    mmin = min(positions)
    mmax = max(positions)
    for t in range(mmin, mmax + 1):
        current = 0
        for p in positions:
            current += abs(t - p)
        if current < result:
            result = current
    return result


def fuel2(positions):
    result = float("inf")
    mmin = min(positions)
    mmax = max(positions)
    cache = [sum(range(i)) for i in range(1, mmax + 2)]
    for t in range(mmin, mmax + 1):
        current = 0
        for p in positions:
            current += cache[abs(t - p)]
        if current < result:
            result = current
    return result


example = """16,1,2,0,4,2,7,1,2,14"""


def test_fuel_example():
    positions = utils.Vector(example)
    actual = fuel(positions)
    expected = 37

    assert actual == expected


def test_fuel():
    positions = getInput()
    actual = fuel(positions)
    expected = 323647

    assert actual == expected


def test_fuel2_example():
    positions = utils.Vector(example)
    actual = fuel2(positions)
    expected = 168

    assert actual == expected


def test_fuel2():
    positions = getInput()
    actual = fuel2(positions)
    expected = 87640209

    assert actual == expected
