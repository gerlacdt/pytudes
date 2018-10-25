from collections import deque


def spinlock(steps=3, N=2017):
    d = deque([0], N+1)
    pos = 0
    for i in range(1, N + 1):
        index = (pos + steps) % len(d)
        pos = index + 1
        d.insert(pos, i)
    return d[pos + 1]
