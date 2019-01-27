from itertools import product
from collections import defaultdict
from utils import rangei, X, Y

serial = input11 = 2866

# norvig's solution

def power_level(point):
    "Follow the rules for power level."
    id = X(point) + 10
    level = (id * Y(point) + serial) * id
    return (level // 100) % 10 - 5


def total_power(topleft, width=3):
    "Total power in the square with given topleft corner and width."
    x, y = topleft
    square = product(range(x, x + width), range(y, y + width))
    return sum(map(power_level, square))


def maxpower(bounds=300, width=3):
    "Return (power, topleft, width) of square within `bounds` of maximum power."
    toplefts = product(rangei(1, bounds - width), repeat=2)
    return max((total_power2(topleft, width), topleft, width)
               for topleft in toplefts)


def summed_area(side, key):
    "A summed-area table. See: https://en.wikipedia.org/wiki/Summed-area_table"
    I = defaultdict(int)
    for x, y in product(side, side):
        I[x, y] = key((x, y)) + I[x, y - 1] + I[x - 1, y] - I[x - 1, y - 1]
    return I


def total_power2(topleft, width=3, I=summed_area(rangei(1, 300), power_level)):
    "Total power in square with given topleft corner and width (from `I`)."
    x, y = topleft
    xmin, ymin, xmax, ymax = x - 1, y - 1, x + width - 1, y + width - 1
    return I[xmin, ymin] + I[xmax, ymax] - I[xmax, ymin] - I[xmin, ymax]
