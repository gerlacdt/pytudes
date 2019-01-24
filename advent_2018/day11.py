input11 = 2866
test_serial = 8


def power(serial, coord):
    x, y = coord
    rackId = x + 10
    level = rackId * y
    level += serial
    level *= rackId
    level = (level // 100) % 10
    level -= 5
    return level


def max_total(grid):
    levels = []
    for y in range(len(grid)-2):
        for x in range(len(grid)-2):
            total = sum([grid[y2][x2] for y2 in range(y, y+3)
                         for x2 in range(x, x+3)])
            levels.append((total, (x, y)))
    total, (x, y) = max(levels)
    return total, (x+1, y+1)


def gen_grid(serial, n):
    grid = []
    for y in range(n):
        grid.append([])
        for x in range(n):
            grid[y].append(power(serial, (x+1, y+1)))
    return grid


def part1(serial=test_serial, n=300):
    grid = gen_grid(serial, n)
    return max_total(grid)
