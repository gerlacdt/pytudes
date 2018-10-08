from collections import deque

# read input
# build graph from input
# get length(nodes)
# do DFS from all nodes and count visited nodes
# if all nodes are visited from a node, this must be the root


input1 = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''


def getKey(node):
    return node[0] if node else ''


def getWeight(node):
    return int(node[1])


def getAdjacents(node):
    return node[2]


def build_tree(s):
    '''Reads a string input and builds the tree. A tree node is triple of
the key, the weight and the adjacent edges. E.g. (key, weight, (tuple
to other keys))
    '''
    lines = s.splitlines()
    acc = {}
    for line in lines:
        words = line.split()
        adjacents = []
        if len(words) > 2 and words[2] == '->':
            adjacents = ''.join(words[3:]).split(',')
        acc[words[0]] = ((words[0], words[1][1:len(words[1]) - 1], adjacents))
    return acc


def dfs(graph, node, collectFn=lambda graph, n: getKey(n)):
    '''Run through the given tree/graph and collect all visited nodes.'''
    stack = [node]  # start with given node
    visited = set()
    collected = []

    # loop as long as stack is non-empty
    while stack:
        v = stack.pop()
        if getKey(v) not in visited:
            visited.add(getKey(v))
            collected.append(collectFn(graph, v))
            for n in [graph[key] for key in getAdjacents(v)]:
                stack.append(n)
    return collected


def bfs(graph, node, collectFn=lambda graph, n, parent: getKey(n)):
    queue = deque([(None, node)])
    visited = set()
    collected = []

    while queue:
        parent, v = queue.popleft()
        visited.add(getKey(v))
        collected.append(collectFn(graph, v, parent))
        for n in [graph[key] for key in getAdjacents(v)]:
            queue.append((v, n))
    return collected


def findRoot(s):
    tree = build_tree(s)
    length = len(tree)

    # for all nodes try dfs, if len(visited) == len(tree) must be the root
    for key, node in tree.items():
        visited = dfs(tree, node)
        if len(visited) == length:
            return node

    return None


def part2(s):
    tree = build_tree(s)
    root = findRoot(s)

    def fn(graph, n, parent):
        children = [graph[key] for key in getAdjacents(n)]
        weights = [getWeight(n)] + [getWeight(child) for child in children]
        return (getKey(parent), getKey(n), weights, sum(weights))

    nodes_with_weights = bfs(tree, root,
                             collectFn=fn)

    return nodes_with_weights
