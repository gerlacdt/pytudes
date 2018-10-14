DIRECTIONS = ('n', 'ne', 'se', 's', 'sw', 'nw')  # directions, ordered clockwise


def parent(direction):
    opposites = {
        'n': 's',
        's': 'n',
        'ne': 'sw',
        'sw': 'ne',
        'nw': 'se',
        'se': 'nw'
    }
    return opposites[direction]  # KeyError if direction not found


def createNumberGenerator():
    '''Creates a sequential number generator. Alyways increments by one
for the next call.'''
    counter = 0
    while True:
        counter += 1
        yield counter


def build_graph(directions):
    graph = {}
    # build graph with 5 children (n, nw, ne, s, sw, se) and parent
    # root has no parent
    # assign a unique to key to every node

    # parent is always opposite directions

    return graph


def hexes(input1):
    # readFile and return tuples of directions

    # build_graph()

    # bfs() goal is last node during graph building

    # bfs finds shortest path (if not try A* star?!?)
    return None
