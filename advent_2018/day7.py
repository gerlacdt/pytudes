from utils import Inputstr, cat
from collections import defaultdict, deque
from itertools  import count as count_from

input7 = Inputstr(7)

test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""


def getPairs(content=test_input):
    lines = content.splitlines()
    steps = [line.split() for line in lines]
    return [(s[1], s[7]) for s in steps]

# norvig solution
def multimap(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def maxval(dic): return max(dic.values())


def order(pairs):
    "Yield steps in order, respecting (before, after) pairs; break ties lexically."
    steps = {step for pair in pairs for step in pair} # Steps remaining to be done
    prereqs = multimap((A, B) for [B, A] in pairs)    # prereqs[A] = [B, ...]
    def ready(step): return all(pre not in steps for pre in prereqs[step])
    while steps:
        step = min(filter(ready, steps))
        steps.remove(step)
        yield step


infinity = float('inf')


def quantify(iterable, pred=bool):
    "Count how many times the predicate is true of an item in iterable."
    return sum(map(pred, iterable))


def schedule(pairs, workers=5):
    "Return a {step:endtime} map for best schedule, given a number of `workers`."
    steps = {step for pair in pairs for step in pair} # Steps remaining to be done
    prereqs = multimap((A, B) for (B, A) in pairs)    # prereqs[A] = [B, ...]
    endtime = {step: infinity for step in steps}      # endtime[step] = time it will be completed
    for t in count_from(0):
        # Assign available steps to free workers
        def ready(step): return all(endtime[p] < t for p in prereqs[step])
        available = filter(ready, steps)
        for step in sorted(available)[:workers]:
            endtime[step] = t + 60 + ord(step) - ord('A')
            steps.remove(step)
            workers -= 1
        # Discover if any workers become free this time step
        workers += quantify(endtime[step] == t for step in endtime)
        # Return answer once all steps have been scheduled
        if not steps:
            return endtime
