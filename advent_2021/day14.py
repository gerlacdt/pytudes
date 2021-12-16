import utils

from collections import deque, Counter, namedtuple


def getInput():
    return utils.Inputstr("14")


def getPolymer(text):
    lines = text.splitlines()
    template = lines[0]
    rules = {}
    for i in range(2, len(lines)):
        pair = lines[i].split("->")
        rules[pair[0].strip()] = pair[1].strip()
    return template, rules


def step(counts, rules):
    result = {}

    return result


def polymerize(template, rules, steps=10):
    counts = Counter(template)
    for i in range(steps):
        counts = step(counts, rules)
    return max(counts.values()) - min(counts.values())


example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def test_getPolymer():
    template, rules = getPolymer(example)
    assert template == "NNCB"
    assert len(rules) == 16


Case = namedtuple(
    "Case",
    ["steps", "expected", "p"],
)


def test_polymerize_example():
    template, rules = getPolymer(example)
    cases = [
        Case(1, 1),
        Case(2, 5),
        Case(3, 7),
        Case(4, 18),
        Case(10, 1588),
        # Case(40, 2188189693529),
    ]
    for c in cases:
        actual = polymerize(template, rules, c.steps)
        assert actual == c.expected, "Case: {}".format(c)


def test_polymerize():
    template, rules = getPolymer(getInput())
    actual = polymerize(template, rules, 10)
    assert actual == 2768
