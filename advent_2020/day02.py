import utils
from collections import namedtuple, Counter

Item = namedtuple("Item", ["min", "max", "char", "password"])


def getInput():
    rules = utils.Array(utils.Inputstr("02"))
    items = []
    for r in rules:
        # split first with "-" get min max
        minMax = [int(num) for num in r[0].split("-")]

        # remove : from second
        char = r[1][:-1]

        # third is password
        password = r[2]
        items.append(Item(minMax[0], minMax[1], char, password))

    return items


def minMaxStrategy(item):
    minn, maxx, char, password = item
    counts = Counter(password)
    if counts[char] < minn or counts[char] > maxx:
        return False
    return True


def positionStrategy(item):
    pos1, pos2, char, password = item

    if password[pos1 - 1] == char and password[pos2 - 1] == char:
        return False
    elif password[pos1 - 1] == char or password[pos2 - 1] == char:
        return True
    return False


def validPasswords(items, validationStrategy=minMaxStrategy):
    return len([item for item in items if validationStrategy(item)])


def test1():
    items = getInput()
    actual = validPasswords(items)
    assert actual == 434


def test2():
    items = getInput()
    actual = validPasswords(items, positionStrategy)
    assert actual == 0
