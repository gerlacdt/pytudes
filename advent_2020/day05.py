import utils


def getInput():
    return utils.Inputstr("05").splitlines()


LINES = getInput()


def seats(lines):
    result = []
    for line in lines:
        rowLow, rowHigh = 0, 127
        colLow, colHigh = 0, 7

        for i in range(0, 7):
            c = line[i]
            if c == "F":
                mid = (rowLow + rowHigh) // 2
                rowHigh = mid
            elif c == "B":
                mid = (rowLow + rowHigh) // 2
                rowLow = mid + 1
            else:
                raise RuntimeError(f"Invalid row: {line}")

        for i in range(7, 10):
            c = line[i]
            if c == "L":
                mid = (colLow + colHigh) // 2
                colHigh = mid
            elif c == "R":
                mid = (colLow + colHigh) // 2
                colLow = mid + 1
            else:
                raise RuntimeError(f"Invalid col: {line}")
        result.append((rowLow, colLow))

    return result


def part1(lines=LINES):
    return max([(row * 8) + col for row, col in seats(lines)])


def part2(lines=LINES):
    seat = [(row * 8) + col for row, col in seats(lines) if row != 0 and row != 127]
    seat.sort()

    for i in range(1, len(seat) - 1):
        prev = seat[i - 1]
        current = seat[i]
        if prev + 1 == current:
            continue
        else:
            return current - 1
    return None


def testPart1():
    actual = part1()
    expected = 885
    assert actual == expected


def testPart2():
    actual = part2()
    expected = 623
    assert actual == expected
