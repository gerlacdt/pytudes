import utils


def getInput(text):
    return utils.Array(text)


def make_grid(lines):
    maxX = maxY = 0
    for line in lines:
        x1, y1, _, x2, y2 = line
        if x1 > maxX:
            maxX = x1
        if x2 > maxX:
            maxX = x2
        if y1 > maxY:
            maxY = y1
        if y2 > maxY:
            maxY = y2

    grid = [[0 for j in range(maxX + 1)] for _ in range(maxY + 1)]
    return grid


def printGrid(grid):
    for row in grid:
        for col in row:
            print("{}".format(col), end="")
        print("")


def vents(lines, diagonal=False):
    grid = make_grid(lines)
    result = 0
    for line in lines:
        # x's are cols
        # y's are rows
        x1, y1, _, x2, y2 = line
        if x1 == x2:
            # go vertical
            if y2 < y1:
                y2, y1 = y1, y2
            for i in range(y1, y2 + 1):
                if grid[i][x1] == 1:
                    result += 1
                grid[i][x1] += 1
        elif y1 == y2:
            # go horizontal
            if x2 < x1:
                x2, x1 = x1, x2
            for j in range(x1, x2 + 1):
                if grid[y1][j] == 1:
                    result += 1
                grid[y1][j] += 1
        else:
            if diagonal:
                # go diagonal
                negative_slope = False
                if x2 < x1 and y2 < y1:
                    x2, x1 = x1, x2
                    y2, y1 = y1, y2
                elif x2 > x1 and y2 < y1:
                    negative_slope = True
                elif x2 < x1 and y2 > y1:
                    x2, x1 = x1, x2
                    y2, y1 = y1, y2
                    negative_slope = True
                i = y1
                j = x1

                while j <= x2:
                    if grid[i][j] == 1:
                        result += 1
                    grid[i][j] += 1
                    i += -1 if negative_slope else 1
                    j += 1
    return result


example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_vents_example():
    actual = vents(getInput(example))

    expected = 5
    assert actual == expected


def test_vents():
    actual = vents(getInput(utils.Inputstr("05")))

    expected = 5084
    assert actual == expected


def test_vents_diagonal_example():
    actual = vents((getInput(example)), diagonal=True)

    expected = 12
    assert actual == expected


def test_vents_diagonal():
    actual = vents(getInput(utils.Inputstr("05")), diagonal=True)

    expected = 17882
    assert actual == expected
