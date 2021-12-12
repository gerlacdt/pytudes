import utils

from collections import defaultdict, namedtuple, Counter
from typing import List


def getInput():
    return utils.Inputstr("12")


def toGraph(text):
    graph = defaultdict(set)
    for line in text.splitlines():
        src, target = line.split("-")
        graph[src].add(target)
        graph[target].add(src)
    return graph


def successors(graph, assignment: List[str]):
    current = assignment[-1]
    succs = graph[current]
    return [s for s in succs if (s not in assignment or s.isupper()) and s != current]


def successors2(graph, assignment: List[str]):
    current = assignment[-1]
    succs = graph[current]
    counts = Counter(assignment)
    alreadyTwice = (
        sum((1 for key, val in counts.items() if key.islower() and val > 1)) > 1
    )

    def isValid(s):
        if s == current:
            # loops are not allowed
            return False
        if s == "start":
            # return to start is not allowd
            return False
        if s == "end" and counts[s] > 0:
            # end cannot have successors
            return False
        if s.islower() and counts[s] > 1:
            # triple accessing node is not allowed
            return False
        if alreadyTwice:
            # accessing twice is not allowed
            return False
        return True

    return [s for s in succs if isValid(s)]


def cave_paths(graph, succsFn):
    paths = []
    goal = "end"

    def helper(assignment):
        if assignment[-1] == goal:
            paths.append(assignment)
            return

        for succ in succsFn(graph, assignment):
            helper(assignment + [succ])

    start = "start"
    helper([start])

    return len(paths)


Case = namedtuple(
    "Case",
    ["example", "expected"],
)

example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def test_cave_paths_example():
    cases = [
        Case(example, 10),
        Case(example2, 19),
        Case(example3, 226),
    ]

    for c in cases:
        graph = toGraph(c.example)
        actual = cave_paths(graph, successors)
        assert actual == c.expected, "Case: {}".format(c)


def test_toGraph():
    actual = toGraph(example)

    assert len(actual) == 6


def test_cave_paths():
    graph = toGraph(getInput())
    actual = cave_paths(graph, successors)

    assert actual == 4378


def test_cave_paths2_example():
    cases = [
        Case(example, 36),
        Case(example2, 103),
        Case(example3, 3509),
    ]

    for c in cases:
        graph = toGraph(c.example)
        actual = cave_paths(graph, successors2)
        assert actual == c.expected, "Case: {}".format(c)


def test_cave_paths2():
    graph = toGraph(getInput())
    actual = cave_paths(graph, successors2)

    assert actual == 133621
