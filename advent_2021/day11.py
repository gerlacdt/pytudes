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


def gridToString(grid):
    s = ""
    for row in grid:
        s += "".join([str(val) for val in row]) + "\n"
    return s[:-1]


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
    return len(flashed)


def count_flashes(grid, steps=100):
    total_flushes = 0
    for i in range(steps):
        total_flushes += step(grid)

    return total_flushes


def count_flashes_sync(grid, steps):
    total_flushes = len(grid) * len(grid[0])
    for i in range(steps):
        if total_flushes == step(grid):
            return i + 1

    return None


simple_example = """11111
19991
19191
19991
11111"""


def test_simple_example():
    expected_step1 = """34543
40004
50005
40004
34543"""

    expected_step2 = """45654
51115
61116
51115
45654"""

    # one step
    grid = toGrid(simple_example)
    actual = count_flashes(grid, 1)
    assert actual == 9

    # two steps
    grid = toGrid(simple_example)
    actual = count_flashes(grid, 2)
    assert grid == toGrid(expected_step2)
    assert actual == 9


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


def test_count_flashes_example_steps():
    grid = toGrid(example)
    actual = count_flashes(grid, 1)

    expected_step1 = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""

    assert gridToString(grid) == expected_step1, "step 1 failed"

    expected_step2 = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""

    grid = toGrid(example)
    actual = count_flashes(grid, 2)

    assert gridToString(grid) == expected_step2, "step 2 failed"


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
    actual = count_flashes_sync(grid, 200)
    assert actual == 195


def test_count_flashes_sync():
    grid = toGrid(getInput())
    actual = count_flashes_sync(grid, 2000)
    assert actual == 276
