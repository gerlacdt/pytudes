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
    stack = [node]  # start with given node
    visited = set()

    # loop as long as stack is non-empty
    while stack:
        v = stack.pop()
        if keyFn(v) not in visited:
            visited.add(keyFn(v))
            for n in [graph[key] for key in successorsFn(v)]:
                stack.append(n)
    return visited


def bfs(graph, node, keyFn, successorsFn):
    '''Do a breath-first-search on the given graph from the given node and
return all visited nodes.'''
    queue = deque([(None, node)])
    visited = set()

    while queue:
        parent, v = queue.popleft()
        if keyFn(v) not in visited:
            visited.add(keyFn(v))
            for n in [graph[key] for key in successorsFn(v)]:
                queue.append((v, n))
    return visited
