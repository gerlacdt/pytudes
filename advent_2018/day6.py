from utils import Inputstr, mapt, flatten

test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""

input6 = Inputstr(6)


def manhatten_distance(p1, p2):
    """Returns the manhatten distance of the two given points. A point is
a tuple with 2 integers."""
    y1, x1 = p1
    y2, x2 = p2
    return abs(x1-x2) + abs(y1-y2)


def getMinCoordinate(distances):
    minimum = min(distances)
    if distances.count(minimum) > 1:
        return -1
    else:
        return distances.index(minimum)


def part1(content=test_input):
    # parse coordinates
    coordinates = [mapt(int, line.split(',')) for line in content.splitlines()]
    coordinates = [(c[1], c[0]) for c in coordinates]  # switch y <-> x, so they match with list indices

    maxy, miny = max(coordinates, key=lambda c: c[0])[0], min(coordinates, key=lambda c: c[0])[0]
    maxx, minx = max(coordinates, key=lambda c: c[1])[1], min(coordinates, key=lambda c: c[1])[1]

    # create grid-array
    arr = [[] for i in range(maxy+1)]
    for i in range(maxy+1):
        for j in range(maxx+1):
            arr[i].append(None)

    # places coordinates in array
    for i, c in enumerate(coordinates):
        y, x = c
        arr[y][x] = i

    # fill grid with coordinates (-1 means: does not belong
    # to any coordinates)
    for y in range(maxy+1):
        for x in range(maxx+1):
            if arr[y][x] != -1:
                # calculate nearest chronal coordinate, if there are more than 1 leave field as None
                distances = [manhatten_distance(c, (y,x)) for c in coordinates]
                arr[y][x] = getMinCoordinate(distances)

    # get non-infinite indexes, i.e. they don't appear at border x ==
    # 0, y == 0, y == maxy, x == maxx
    infinteIndices = {arr[y][x] for y in range(maxy+1) for x in range(maxx+1)
                    if x == 0 or y == 0
                    or x == maxx or y == maxy or arr[y][x] == -1}

    validIndices = set(range(len(coordinates))) - infinteIndices

    flat = list(flatten(arr))
    return max(flat.count(valid) for valid in validIndices)


def part2(content=test_input):
    pass
