from utils import Inputstr, cat
from collections import defaultdict, deque
import re


input7 = Inputstr(7)

test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""


# norvig solution
def multimap(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def order(content=test_input):
    lines = content.splitlines()
    steps = [line.split() for line in lines]
    pairs = [(s[1], s[7]) for s in steps]
    "Yield steps in order, respecting (before, after) pairs; break ties lexically."
    steps = {step for pair in pairs for step in pair} # Steps remaining to be done
    prereqs = multimap((A, B) for [B, A] in pairs)    # prereqs[A] = [B, ...]
    def ready(step): return all(pre not in steps for pre in prereqs[step])
    while steps:
        step = min(filter(ready, steps))
        steps.remove(step)
        yield step
