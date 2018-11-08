# coding: utf-8

from collections import namedtuple

iterations = 12861455

R, L = 1, -1

Command = namedtuple('Command', ['value', 'move', 'nextState'])


# command table
ctable = {
    ('A', 0): Command(value=1, move=R, nextState='B'),
    ('A', 1): Command(value=0, move=L, nextState='B'),

    ('B', 0): Command(value=1, move=L, nextState='C'),
    ('B', 1): Command(value=0, move=R, nextState='E'),

    ('C', 0): Command(value=1, move=R, nextState='E'),
    ('C', 1): Command(value=0, move=L, nextState='D'),

    ('D', 0): Command(value=1, move=L, nextState='A'),
    ('D', 1): Command(value=1, move=L, nextState='A'),

    ('E', 0): Command(value=0, move=R, nextState='A'),
    ('E', 1): Command(value=0, move=R, nextState='F'),

    ('F', 0): Command(value=1, move=R, nextState='E'),
    ('F', 1): Command(value=1, move=R, nextState='A'),
}


testtable = {
    ('A', 0): Command(value=1, move=R, nextState='B'),
    ('A', 1): Command(value=0, move=L, nextState='A'),
    ('B', 0): Command(value=1, move=L, nextState='A'),
    ('B', 1): Command(value=1, move=R, nextState='A'),
}


def turing(table, N=1):
    position = 0
    state = 'A'
    ones = set()
    for i in range(N):
        value = 1 if position in ones else 0
        c = table[(state, value)]
        if c.value == 1:
            ones.add(position)
        else:
            ones.discard(position)
        position += c.move
        state = c.nextState

    return len(ones)


# assert(turing(ctable, iterations) == 3778)
