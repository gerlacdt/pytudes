from functools import reduce
from utils import cat
from day10 import knothash


def toBin(char):
    d = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111',
    }
    return d[char]


def defrag(input1, N=128):
    lines = [knothash("{}-{}".format(input1, i)) for i in range(N)]
    binaryhash = [cat(map(toBin, line)) for line in lines]
    return reduce(lambda acc, c:  acc + 1 if c == '1' else acc, cat(binaryhash), 0)


def region(input1, N=128):
    lines = [knothash("{}-{}".format(input1, i)) for i in range(N)]
    binaryhash = [cat(map(toBin, line)) for line in lines]
    return dfs(binaryhash)


def dfs(graph):
    stack = []  # start with given node
    visited = set()
    nodes = [(x, y) for x in range(len(graph)) for y in range(len(graph[0]))]
    groups = set()
    for node in nodes:
        x, y = node
        group = set()
        if graph[x][y] == '1':
            stack.append(node)
        while stack:
            v = stack.pop()
            if v not in visited:
                group.add(v)
                visited.add(v)
                for key in successors(graph, v):
                    group.add(v)
                    stack.append(key)
        if group != set():
            groups.add(tuple(group))
    return len(groups)


def successors(grid, state):
    x, y = state
    lengthx = len(grid)
    lengthy = len(grid[0])
    succs = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

    def valid(pos):
        x, y = pos
        return 0 <= x and 0 <= y and x < lengthx and y < lengthy and grid[x][y] == '1'

    return filter(valid, succs)
