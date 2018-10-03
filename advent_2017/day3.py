import utils


def findCenter(arr):
    '''Finds the center of the matrix. Center is defined where the value 1
is.'''
    for x, line in enumerate(arr):
        for y, val in enumerate(line):
            if val == 1:
                return x, y
    raise RuntimeError('No center exist with value 1')


def calcManhattanDistance(orig, dest):
    '''Returns the manhattan distance of two points. A point is a x,y
tuple'''
    ox, oy = orig[0], orig[1]
    dx, dy = dest[0], dest[1]
    return abs(ox - dx) + abs(oy - dy)


def spiral(s):
    '''Returns the sum of all steps needed to bring all numbers to the
center.'''
    rows = utils.Array(s)
    ox, oy = findCenter(rows)

    # for all from 0,0 find way to 1, count steps
    acc = 0
    for x, line in enumerate(rows):
        for y, val in enumerate(line):
            if val == 1:
                continue
            dist = calcManhattanDistance((ox, oy), (x, y))
            print("({}, {},  val: {} => dist {})".format(x, y, val, dist))
            acc += dist

    # sum all steps return from all numbers
    return acc
