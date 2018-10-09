# coding: utf-8

from collections import deque, Counter
from utils import Ø, groupby, flatten, first
import re


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


def norvig_towers(lines):
    "Return (weight, above) dicts."
    weight = {}
    above = {}
    for line in lines:
        name, w, *rest = re.findall(r'\w+', line)
        weight[name] = int(w)
        above[name] = set(rest)
    return weight, above


def norvig_root(input1):
    lines = input1.splitlines()
    weight, above = norvig_towers(lines)
    programs = set(above)

    return programs - set(flatten(above.values()))


def norvig_part2(input1):
    lines = input1.splitlines()
    weight, above = norvig_towers(lines)
    programs = set(above)

    below = {a: b for b in programs for a in above[b]}

    def tower_weight(p):
        "Total weight for the tower whose root (bottom) is p."
        return weight[p] + sum(map(tower_weight, above[p]))


    def siblings(p):
        "The other programs at the same level as this one."
        if p not in below:
            return Ø  # the root has no siblings
        else:
            return above[below[p]] - {p}  # remove itself from sibling result set


    def wrong(p):
        return tower_weight(p) not in map(tower_weight, siblings(p))


    def wrongest(programs):
        return first(p for p in programs
                     if wrong(p)
                     and not any(wrong(p2) for p2 in above[p]))


    def correct(p):
        """Return the weight that would make p's tower's weight the same as
        its sibling towers."""
        delta = tower_weight(first(siblings(p))) - tower_weight(p)
        return weight[p] + delta

    return correct(wrongest(programs))
