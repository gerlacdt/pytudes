from collections import deque
from itertools import islice


def readFile(filename):
    '''Read whole file with filename into a string and returns it.'''
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def dfs(graph, node, keyFn, successorsFn):
    '''Do a depth-first-search on the given graph from the given node and
return all visited nodes.
    '''
    stack = [keyFn(node)]  # start with given node
    visited = set()

    # loop as long as stack is non-empty
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for key in successorsFn(v):
                stack.append(key)
    return visited


def bfs(graph, node, keyFn, successorsFn):
    '''Do a breath-first-search on the given graph from the given node and
return all visited nodes.'''
    queue = deque([keyFn(node)])
    visited = set()

    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            for key in successorsFn(v):
                queue.append(key)
    return visited
