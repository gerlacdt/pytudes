import utils
from functools import reduce
import operator


def getInput():
    lines = utils.Inputstr("09")
    grid = [[int(c) for c in list(line)] for line in lines.splitlines()]
    return grid


def isValid(point, grid):
    maxRow = len(grid)
    maxCol = len(grid[0])
    row, col = point
    if row >= 0 and row < maxRow and col >= 0 and col < maxCol:
        return True
    return False


def low_points(grid):
    result = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            points = [n for n in utils.neighbors4((i, j)) if isValid(n, grid)]
            if all([col < grid[y][x] for y, x in points]):
                result.append((i, j))
    return result


def heightmap(grid):
    return sum([grid[y][x] + 1 for y, x in low_points(grid)])


def basin(grid):
    def successors(point):
        y, x = point
        return [
            (y + y1, x + x1)
            for y1, x1 in utils.HEADINGS
            if isValid((y + y1, x + x1), grid) and grid[y + y1][x + x1] != 9
        ]

    def dfs(start):
        visited = set()
        size = 0
        frontier = [start]
        while frontier:
            point = frontier.pop()
            if point in visited:
                continue
            size += 1
            visited.add(point)
            for succ in successors(point):
                if succ not in visited:
                    frontier.append(succ)
        return size

    result = sorted([dfs(start) for start in low_points(grid)])[-3:]
    return reduce(operator.mul, result)


example = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_heightmap_low_points_example():
    grid = [[int(c) for c in list(line)] for line in example.splitlines()]
    actual = heightmap(grid)
    assert actual == 15


def test_heightmap_low_points():
    grid = getInput()
    actual = heightmap(grid)
    assert actual == 522


def test_basin_example():
    grid = [[int(c) for c in list(line)] for line in example.splitlines()]
    actual = basin(grid)
    assert actual == 1134


def test_basin():
    grid = getInput()
    actual = basin(grid)
    assert actual == 916688
