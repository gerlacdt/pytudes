import utils
from functools import reduce


def getInput():
    lines = utils.Inputstr("09")
    grid = [[int(c) for c in list(line)] for line in lines.splitlines()]
    return grid


def low_points(grid):
    result = []
    maxRow = len(grid)
    maxCol = len(grid[0])

    def isValid(point):
        row, col = point
        if row >= 0 and row < maxRow and col >= 0 and col < maxCol:
            return True
        return False

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            points = [n for n in utils.neighbors4((i, j)) if isValid(n)]
            if all([col < grid[y][x] for y, x in points]):
                result.append(col)
    return sum([risk + 1 for risk in result])


def basin(grid):
    # find start points
    start_points = []
    maxRow = len(grid)
    maxCol = len(grid[0])

    def isValid(point):
        row, col = point
        if row >= 0 and row < maxRow and col >= 0 and col < maxCol:
            return True
        return False

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            points = [n for n in utils.neighbors4((i, j)) if isValid(n)]
            if all([col < grid[y][x] for y, x in points]):
                start_points.append((i, j))

    def successors(point):
        y, x = point

        return [
            (y + y1, x + x1)
            for y1, x1 in utils.HEADINGS
            if isValid((y + y1, x + x1)) and grid[y + y1][x + x1] != 9
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
            # print("point: {}".format(point))
            # print("val: {}".format((grid[point[0]][point[1]])))
            # print("frontier: {}".format(frontier))
            # print("visited: {}".format(visited))
            for succ in successors(point):
                if succ not in visited:
                    frontier.append(succ)
        # print()
        return size

    result = sorted([dfs(start) for start in start_points])[-3:]
    return reduce(lambda acc, x: acc * x, result)


example = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_low_points_example():
    grid = [[int(c) for c in list(line)] for line in example.splitlines()]
    actual = low_points(grid)
    assert actual == 15


def test_low_points():
    grid = getInput()
    actual = low_points(grid)
    assert actual == 522


def test_basin_example():
    grid = [[int(c) for c in list(line)] for line in example.splitlines()]
    actual = basin(grid)
    assert actual == 1134


def test_basin():
    grid = getInput()
    actual = basin(grid)
    assert actual == 916688
