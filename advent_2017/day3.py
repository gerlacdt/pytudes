import utils
import math
from itertools import islice


def move(position, direction):
    '''Move one step from the given to position to the given direction.'''
    x, y = position
    if direction == 'up':
        return (x - 1, y)
    elif direction == 'down':
        return (x + 1, y)
    elif direction == 'left':
        return (x, y - 1)
    elif direction == 'right':
        return (x, y + 1)
    raise RuntimeError("Given directions does not exist: {}".format(direction))


def nextDirection(direction):
    '''Return the next direction if a direction change is requested.'''
    if direction == 'up':
        return 'left'
    elif direction == 'down':
        return 'right'
    elif direction == 'left':
        return 'down'
    elif direction == 'right':
        return 'up'
    raise RuntimeError("Given directions does not exist: {}".format(direction))


def grid(n):
    '''generates a spiral grid with 1 as center number'''
    if n % 2 == 0:
        raise RuntimeError("Given grid-size must be an odd number: {}.format(n)")

    currentStepsLeft = 0
    currentDirection = 'down'  # initial direction, switch in first iteration to 'right
    maxSteps = 0

    # initial empty grid with center number 1
    center = n - 1
    currentPosition = (center // 2, center // 2)
    grid = [[0 for i in range(center + 1)] for j in range(center + 1)]
    grid[currentPosition[0]][currentPosition[1]] = 1

    # fill zero grid with numbers
    for i in range(2, (n ** 2) + 1):
        if currentStepsLeft == 0:
            currentDirection = nextDirection(currentDirection)
            if currentDirection == 'left' or currentDirection == 'right':
                maxSteps += 1
            currentStepsLeft = maxSteps
        currentPosition = move(currentPosition, currentDirection)
        x, y = currentPosition
        grid[x][y] = i
        currentStepsLeft -= 1
    return grid


def spiral(qn):
    '''Returns the manhatten distance for a given number qn in a spriral
grid which is generated from n. The the grid will have n^2 fields. n
must be odd in order to generate a correct spiral from the inner to
outside with the start value of 1.

Example:
spriral(33, 1023) => 31
spriral(5, 1) => 0
spriral(5, 17) => 4
    '''
    # find grid size
    n = int(math.sqrt(qn))
    n += 1
    if n % 2 == 0:
        n += 1

    g = grid(n)
    center = (n // 2, n // 2)
    # find requested number in grid
    position = ()
    for i, line in enumerate(g):
        for j, val in enumerate(line):
            if val == qn:
                position = (i, j)

    if position == ():
        raise RuntimeError("requested number not in grid")

    # calc distance from center
    dist = calcManhattanDistance(center, position)
    return dist


def calcManhattanDistance(orig, dest):
    '''Returns the manhattan distance of two points. A point is a x,y
tuple'''
    ox, oy = orig[0], orig[1]
    dx, dy = dest[0], dest[1]
    return abs(ox - dx) + abs(oy - dy)


HEADINGS = UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)


def norvig_spiral():
    '''Yield successive (x, y) coordinates of squares on a spiral.
    Example: list(itertools.islice(spiral(), 10))
'''
    x = y = s = 0
    yield (0, 0)
    while True:
        for (dx, dy) in (RIGHT, UP, LEFT, DOWN):
            if dy:
                s += 1  # increment side length before RIGHT and LEFT
            for _ in range(s):
                x += dx
                y += dy
                yield(x, y)


def norvig_solve(M):
    coords = utils.nth(norvig_spiral(), M - 1)
    return utils.cityblock_distance(coords)
