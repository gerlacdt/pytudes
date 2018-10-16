import re
from myutils import dfs


input1 = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''


def part1(string):
    # parse input
    graph = {}
    for line in string.splitlines():
        n, *rest = re.findall(r'\w+', line)
        graph[n] = set(rest)

    def successorFn(graph):
        return lambda x: graph[x]

    visited = dfs(graph, '0', lambda x: x, successorFn(graph))
    # def dfs(graph, node, keyFn, successorsFn):
    return len(visited)


def part2(string):
    # parse input
    graph = {}
    for line in string.splitlines():
        n, *rest = re.findall(r'\w+', line)
        graph[n] = set(rest)

    def successorFn(graph):
        return lambda x: graph[x]

    groups = []
    for key in graph.keys():
        # only start search if key is not in none of allVisited Set
        if not any(key in s for s in groups):
            visited = dfs(graph, key, lambda x: x, successorFn(graph))
            groups.append(visited)
    return len(groups)
