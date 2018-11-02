from utils import flatten, error, map2d
from myutils import readFile


def Enhancements(lines):
    "Create a dict of {grid: enhanced_grid}; include all rotations/flips."
    enhancements = {}
    for line in lines:
        lhs, rhs = map(Pixels, line.split('=>'))
        for rot in range(4):
            enhancements[lhs] = enhancements[flip(lhs)] = rhs
            lhs = rotate(lhs)
    return enhancements


def Pixels(text):
    "Translate the str '.#/.#' to the grid ((0, 1), (0, 1))"
    bits = {'#': 1, '.': 0}
    return tuple(tuple(bits[p] for p in row.strip())
                 for row in text.split('/'))


def rotate(subgrid):
    "Rotate a subgrid 90 degrees clockwise."
    return tuple(zip(*reversed(subgrid)))


def flip(subgrid):
    "Reverse every row of the subgrid."
    return tuple(tuple(reversed(row)) for row in subgrid)


input1 = """../.. => .../.#./.#.
#./.. => .../#../#..
##/.. => #.#/.#./.#.
.#/#. => ##./##./...
##/#. => .##/###/#..
##/## => .##/#../##.
"""

INPUT1 = readFile("./data/input21.txt")
enhancements = Enhancements(INPUT1.splitlines())


def enhance(grid):
    "Divide the drid into pieces, enhance each piece, and stitch them together."
    return stitch_grid(map2d(enhancements.get, divide_grid(grid)))


def divide_grid(grid):
    "Divide the grid into d x d pieces and enhance each piece."
    N = len(grid[0])
    d = (2 if N % 2 == 0 else 3 if N % 3 == 0 else error())
    return [[tuple(row[c:c+d] for row in grid[r:r+d])
             for c in range(0, N, d)]
            for r in range(0, N, d)]


def stitch_grid(pieces):
    "Stitch the pieces back into one big grid."
    N = sum(map(len, pieces[0]))
    return tuple(tuple(getpixel(pieces, r, c)
                       for c in range(N))
                 for r in range(N))


def getpixel(pieces, r, c):
    "The pixel at location (r, c), from a matrix of d x d pieces."
    # Use `//` to find the right piece, and `%` to find the pixel within the piece
    d = len(pieces[0][0])
    piece = pieces[r // d][c // d]
    return piece[r % d][c % d]


grid = Pixels('.#./..#/###')


# results

# part1 : 117
# sum(flatten(repeat(5, enhance, grid)))

# part2 : 2026963
# sum(flatten(repeat(18, enhance, grid)))
