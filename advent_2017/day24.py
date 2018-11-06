from myutils import readFile


input1 = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""


INPUT1 = readFile("./data/input24.txt")


def strength(ports):
    return sum(map(lambda p: sum(p), ports))


def successors(node, ports):
    """Returns all possible succesor for the given node. A node/successor is a 4-tuple.
    (x,y, x-used?, y-used?)
 """
    port = node[-1]
    successors = []
    for p in ports:
        if p[0] == port[1]:
            successors.append((p[0], p[1]))
        elif p[1] == port[1]:
            successors.append((p[1], p[0]))

    nodes = list(node)
    return [tuple(nodes + [s]) for s in successors]


def bridge(input1):
    ports = {tuple(map(int, line.split("/"))) for line in input1.splitlines()}
    ports = set(map(tuple, map(sorted, ports)))
    maxstrength = 0
    maxlength = 1
    maxstrength_longest = []

    # collect startnodes with a 0 pin side
    stack = []
    for p in ports:
        if p[0] == 0:
            stack.append((p,))
        elif p[1] == 0:
            stack.append(((p[1], p[0]),))

    maxstrength_longest.append(stack[0]) # add startnode

    # DFS
    while stack:
        node = stack.pop()
        cstrength = strength(node)
        maxstrength = cstrength if cstrength > maxstrength else maxstrength
        clength = len(node)
        if clength > maxlength:
            maxlength = clength
            maxstrength_longest = []
            maxstrength_longest.append(node)
        elif clength == maxlength:
            maxstrength_longest.append(node)

        for succs in successors(node,
                                ports.difference(set(map(tuple, map(sorted, node))))):
            stack.append(succs)

    return maxstrength, max(list(map(strength, maxstrength_longest)))


assert(bridge(input1) == (31, 19))
# assert(bridge(INPUT1) == 1906, 1824)
