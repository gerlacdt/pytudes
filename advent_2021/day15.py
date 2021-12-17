import utils
import sys

sys.setrecursionlimit(10000)


def getInput():
    return utils.Inputstr("15")


def parse(text):
    lines = text.splitlines()
    grid = [[int(c) for c in line] for line in lines]
    return grid


def isValid(grid, point):
    y, x = point
    maxY = len(grid) - 1
    maxX = len(grid[0]) - 1
    if y > maxY or y < 0:
        return False
    if x > maxX or x < 0:
        return False
    return True


def neighbors(grid, point):
    neighbors = utils.neighbors4(point)
    # filter valid neighbors
    return filter(lambda p: isValid(grid, p), neighbors)


def create_moves_fn(grid):
    def moves_fn(point):
        return neighbors(grid, point)

    return moves_fn


def create_h_fn(grid):
    maxY = len(grid) - 1
    maxX = len(grid[0]) - 1

    def h_fn(point):
        return utils.cityblock_distance((maxX, maxY), point)

    return h_fn


def create_cost_fn(grid):
    def cost_fn(src, target):
        x, y = target
        return grid[y][x]

    return cost_fn


def chiton(grid):
    start = (0, 0)

    path = utils.Astar(
        start,
        create_moves_fn(grid),
        create_h_fn(grid),
        create_cost_fn(grid),
    )

    costs = [grid[y][x] for x, y in path]
    return sum(costs) - costs[0]


def chiton5x5(grid):
    grid5x5 = [[0 for _ in range(5 * len(grid[0]))] for _ in range(5 * len(grid))]

    for i in range(len(grid5x5)):
        for j in range(len(grid5x5[0])):
            val = grid[i % len(grid)][j % len(grid[0])]
            x_mod = i // len(grid)
            y_mod = j // len(grid[0])
            val += x_mod + y_mod
            if val >= 10:
                val %= 10
                val += 1
            grid5x5[i][j] = val

    return chiton(grid5x5)


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


def test_chiton_example():
    grid = parse(example)
    actual = chiton(grid)

    assert actual == 40


def test_chiton():
    grid = parse(getInput())
    actual = chiton(grid)

    assert actual == 537


def test_chiton5x5_example():
    grid = parse(example)
    actual = chiton5x5(grid)

    assert actual == 315


def test_chiton5x5():
    grid = parse(getInput())
    actual = chiton5x5(grid)

    assert actual == 2881
