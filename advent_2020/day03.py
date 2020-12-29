import utils
from functools import reduce
import operator


def getInput():
    s = utils.Inputstr("03")
    return s.splitlines()


GRID = getInput()


def trees(grid=GRID, steps=(1, 3)):
    row = col = 0
    rowSteps, colSteps = steps
    result = 0
    while row < len(grid):
        if grid[row][col] == "#":
            result += 1
        row += rowSteps
        col = (col + colSteps) % len(grid[0])

    return result


def test():
    grid = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()
    actual = trees(grid)
    expected = 7
    assert actual == expected


def testPart1():
    actual = trees(GRID)
    expected = 176
    assert actual == expected


def testPart2():
    steps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    actual = reduce(operator.mul, [trees(GRID, s) for s in steps], 1)
    expected = 5872458240
    assert actual == expected
