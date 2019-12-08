import utils


def getInput():
    lines = utils.Array(utils.Inputstr("03"))
    return parse(lines)


def parse(lines):
    return [[(word[0], int(word[1:])) for word in l] for l in lines]


def move(pos, direction):
    if direction == "R":
        return (pos[0] + 1, pos[1])
    elif direction == "L":
        return (pos[0] - 1, pos[1])
    elif direction == "U":
        return (pos[0], pos[1] - 1)
    elif direction == "D":
        return (pos[0], pos[1] + 1)
    raise RuntimeError("Invalid direction: {}", direction)


def intersect(pos, wire, visited):
    if pos == utils.origin:
        return False
    for i in range(wire):
        if (i, pos) in visited:
            return True
    return False


def findIntersections(lines):
    start = utils.origin
    visited = set([start])
    intersections = set()
    currentpos = start
    for wire, moves in enumerate(lines):
        currentpos = start
        for m in moves:
            direction, steps = m
            for i in range(steps):
                currentpos = move(currentpos, direction)
                if intersect(currentpos, wire, visited):
                    intersections.add(currentpos)
                visited.add((wire, currentpos))
    return intersections


def part1(lines):
    intersections = findIntersections(lines)
    return min([utils.cityblock_distance(ints) for ints in intersections])


def wireWight(intersection, lines):
    weight = 0
    for moves in lines:
        path = 0
        currentpos = utils.origin
        for m in moves:
            direction, steps = m
            for i in range(steps):
                currentpos = move(currentpos, direction)
                path += 1
                if currentpos == intersection:
                    weight += path
                    break
    return weight


def part2(lines):
    intersections = findIntersections(lines)
    return min([wireWight(ints, lines) for ints in intersections])


def test():
    lines = getInput()
    actual = part1(lines)
    expected = 273
    assert actual == expected


def testPart2():
    lines = getInput()
    actual = part2(lines)
    expected = 15622
    assert actual == expected


def testExamples():
    lines = """R8,U5,L5,D3
    U7,R6,D4,L4
    """
    actual = part1(parse(utils.Array(lines)))
    expected = 6
    assert actual == expected

    lines = """R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83
    """
    actual = part1(parse(utils.Array(lines)))
    expected = 159
    assert actual == expected

    lines = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""
    actual = part1(parse(utils.Array(lines)))
    expected = 135
    assert actual == expected


def testPart2Examples():
    lines = """R8,U5,L5,D3
    U7,R6,D4,L4"""
    actual = part2(parse(utils.Array(lines)))
    expected = 30
    assert actual == expected

    lines = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    actual = part2(parse(utils.Array(lines)))
    expected = 610
    assert actual == expected
