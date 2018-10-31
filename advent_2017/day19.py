from utils import letters, cat

UP, LEFT, DOWN, RIGHT = (-1, 0), (0, -1), (1, 0), (0, 1)

input1 = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
"""

LETTERS = letters.upper()


def getHeading(direction):
    if direction == "DOWN":
        return DOWN
    elif direction == "LEFT":
        return LEFT
    elif direction == "UP":
        return UP
    elif direction == "RIGHT":
        return RIGHT
    else:
        raise RuntimeError("Invalid direction")


def newPos(lines, pos, heading):
    p = (pos[0]+heading[0], pos[1]+heading[1])
    if p[0] < 0 or p[0] >= len(lines) or p[1] < 0 or p[1] >= len(lines[0]):
        return None
    return p


def tubes(input1):
    lines = input1.splitlines()
    maxlen = len(max(lines, key=len))
    lines = [line.ljust(maxlen) for line in lines]

    # find beginning
    start = lines[0].index('|')
    direction = "DOWN"
    pos = (0, start)
    collected = []

    def apply(heading):
        nonlocal direction
        char = lines[pos[0]][pos[1]]
        if char == "|" or char == "-":
            # keep directions
            return (pos[0]+heading[0], pos[1]+heading[1])
        elif char in LETTERS:
            #keep directions but collect letter
            collected.append(char)
            return (pos[0]+heading[0], pos[1]+heading[1])
        elif char == "+":
            # change direction, only 1 should be valid
            if direction == "UP" or direction == "DOWN":
                # go left or right
                r = newPos(lines, pos, RIGHT)
                l = newPos(lines, pos, LEFT)
                if r and lines[r[0]][r[1]] != " ":
                    direction = "RIGHT"
                    return r
                elif l and lines[l[0]][l[1]] != " ":
                    direction = "LEFT"
                    return l
                else:
                    raise RuntimeError("Invalid state, char: {}, pos: {}, direction: {}".format(char, pos, direction))
            else:
                # go up or down
                d = newPos(lines, pos, DOWN)
                u = newPos(lines, pos, UP)
                if d and lines[d[0]][d[1]] != " ":
                    direction = "DOWN"
                    return d
                elif u and lines[u[0]][u[1]] != " ":
                    direction = "UP"
                    return u
                else:
                    raise RuntimeError("Invalid state, char: {}, pos: {}, direction: {}".format(char, pos, direction))
        return None

    while pos[0] >= 0 and pos[0] < len(lines):
        # move
        char = lines[pos[0]][pos[1]]
        heading = getHeading(direction)
        pos = apply(heading)
        if not pos:
            break

    return cat(collected)
