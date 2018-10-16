import re

input1 = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''


def dfs(graph, node, successorsFn):
    '''Do a depth-first-search on the given graph from the given node and
return all visited nodes.
    '''
    stack = [node]  # start with given node
    visited = set()

    # loop as long as stack is non-empty
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for key in successorsFn(v):
                stack.append(key)
    return visited


def part1(string):
    # parse input
    graph = {}
    for line in string.splitlines():
        n, *rest = re.findall(r'\w+', line)
        graph[n] = set(rest)

    def successorFn(graph):
        return lambda x: graph[x]

    visited = dfs(graph, '0', successorFn(graph))
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
            visited = dfs(graph, key, successorFn(graph))
            groups.append(visited)
    return len(groups)
