import utils


def getInput():
    commands = utils.Array(utils.Inputstr("02"))
    return commands


def submarine(commands):
    depth = horizontal = 0
    for c in commands:
        direction = c[0]
        val = c[1]
        if direction == "forward":
            horizontal += val
        elif direction == "down":
            depth += val
        elif direction == "up":
            depth -= val
    return horizontal * depth


def submarine2(commands):
    depth = horizontal = aim = 0
    for c in commands:
        direction = c[0]
        val = c[1]
        if direction == "forward":
            horizontal += val
            depth += val * aim
        elif direction == "down":
            aim += val
        elif direction == "up":
            aim -= val
    return horizontal * depth


def test1():
    actual = submarine(getInput())
    expected = 1692075
    assert actual == expected


def test2():
    actual = submarine2(getInput())
    expected = 1749524700
    assert actual == expected
