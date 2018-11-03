from utils import (HEADINGS, UP, DOWN, LEFT, RIGHT,
                   turn_right, turn_left, turn_around, add, repeat)
from myutils import readFile
from collections import namedtuple, defaultdict


input1 = """.........
.........
.........
.....#...
...#.....
.........
.........
.........
""".strip().splitlines()


INPUT1 = readFile("./data/input22.txt").strip().splitlines()
Net = namedtuple('Net', 'current, heading, caused, infected')


def parse_net(lines):
    "Read the initial state of the network."
    lines = list(lines)
    center = (len(lines) // 2, len(lines[0].strip()) // 2)
    return Net(center, UP, 0,
               {(x, y)
                for (y, row) in enumerate(lines)
                for (x, node) in enumerate(row)
                if node == '#'})


def burst(net):
    "Simulate the virus through one step and return the new state of the network."
    (current, heading, caused, infected) = net
    heading = (turn_right if current in infected else turn_left)(heading)
    if current in infected:
        infected.remove(current)
    else:
        caused += 1
        infected.add(current)
    return Net(add(current, heading), heading, caused, infected)


def virus(lines, N=0):
    return repeat(N, burst, parse_net(lines)).caused


assert(virus(input1, N=70) == 41)
assert(virus(INPUT1, N=10000) == 5339)


def burst2(net, N=0):
    "Run N steps of bursts on the network depicted by `lines`."
    (current, heading, caused, infected) = net
    status = defaultdict(lambda: 'C', {pos: 'I' for pos in infected})
    for _ in range(N):
        S = status[current]
        if S == 'C':
            heading = turn_left(heading)
            status[current] = 'W'
        elif S == 'W':
            # heading unchanged
            status[current] = 'I'
            caused += 1
        elif S == 'I':
            heading = turn_right(heading)
            status[current] = 'F'
        elif S == 'F':
            heading = turn_around(heading)
            status[current] = 'C'
        current = add(current, heading)
    return caused


def virus2(lines, N=0):
    return burst2(parse_net(lines), N)


assert(virus2(input1, N=100) == 26)
# assert(virus2(INPUT1, N=10000000) == 2512380)
