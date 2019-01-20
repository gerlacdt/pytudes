from collections import deque
from utils import Inputstr


input9 = Inputstr(9)


def solve1(nplayers=9, nmarbles=25):
    q = deque([0])  # first start with 0 marbles
    currentMarbleIndex = 0
    scores = [0] * (nplayers + 1)

    for i in range(1, nmarbles+1):
        player = i % nplayers
        player = nplayers if player == 0 else player
        if i % 23 == 0:
            newIndex = currentMarbleIndex - 7
            if newIndex < 0:
                newIndex += 1
            scores[player] += i + q[newIndex]
            del q[newIndex]
            currentMarbleIndex = newIndex
        else:
            newIndex = (currentMarbleIndex + 1) % len(q)+1
            if newIndex == 0:
                newIndex = len(q)
            q.insert(newIndex, i)
            currentMarbleIndex = newIndex
        # print("index: {}, player: {}, queue: {}".format(currentMarbleIndex, player, q))

    return max(scores)
