from collections import deque, Counter
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




# norvig's faster solution, needed for part 2

players = 411
marbles = 71058 * 100
expected = 3516007333


def play(players, marbles, verbose=False):
    "Add `marbles` to `circle`, rotating according to rules and scoring every 23 marbles."
    circle = deque([0])
    scores = Counter()
    for m in range(1, marbles):
        player = (m - 1) % players + 1
        if m % 23:
            circle.rotate(-1)
            circle.append(m)
        else:
            circle.rotate(+7)
            scores[player] += circle.pop() + m
            circle.rotate(-1)
        if verbose: print(player, list(circle))
    return max(scores.values())
