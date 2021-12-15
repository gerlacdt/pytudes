import utils


def getInput():
    return utils.Inputstr("15")


def parse(text):
    lines = text.splitlines()
    grid = [[int(c) for c in line] for line in lines]
    return grid


def chiton(grid):
    return 0


example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_chiton():
    grid = parse(example)
    actual = chiton(grid)

    assert actual == 40
