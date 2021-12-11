import utils


def getInput():
    return utils.Inputstr("11")


def toGrid(text):
    grid = []
    for row, line in enumerate(text.splitlines()):
        grid.append([])
        for c in line:
            grid[row].append(int(c))
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
    y, x = point
    neighbors = utils.neighbors8(point)
    # filter valid neighbors
    return filter(lambda p: isValid(grid, p), neighbors)


def inc_neighbors(grid, point):
    points = neighbors(grid, point)
    for p in points:
        y, x = p
        grid[y][x] += 1


def flash(grid, start_points):
    flashed = set()
    frontier = start_points[:]
    while frontier:
        point = frontier.pop()
        y, x = point
        if point in flashed:
            continue
        # flash point
        inc_neighbors(grid, point)
        flashed.add(point)
        for n in neighbors(grid, point):
            succ_y, succ_x = n
            if grid[succ_y][succ_x] > 9 and n not in flashed:
                frontier.append(n)

    return flashed


def step(grid):
    while True:
        # increase by 1
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                grid[y][x] += 1

        # chain reaction flash
        start_points = []
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col > 9:
                    start_points.append((y, x))
        flashed = flash(grid, start_points)

        # set to 0 for all val > 9
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col > 9:
                    grid[y][x] = 0
        yield len(flashed)


def count_flashes(grid, steps=100):
    return sum(next(step(grid)) for i in range(steps))


def count_flashes_sync(grid):
    all_flushes = len(grid) * len(grid[0])
    return next(i + 1 for i, flushes in enumerate(step(grid)) if all_flushes == flushes)


example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_count_flashes_example():
    grid = toGrid(example)
    actual = count_flashes(grid, 10)
    assert actual == 204

    grid = toGrid(example)
    actual = count_flashes(grid, 100)
    assert actual == 1656


def test_count_flashes():
    grid = toGrid(getInput())
    actual = count_flashes(grid, 100)

    assert actual == 1681


def test_count_flashes_sync_example():
    grid = toGrid(example)
    actual = count_flashes_sync(grid)
    assert actual == 195


def test_count_flashes_sync():
    grid = toGrid(getInput())
    actual = count_flashes_sync(grid)
    assert actual == 276
