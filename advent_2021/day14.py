import utils

from collections import deque, Counter, namedtuple


def getInput():
    return utils.Inputstr("14")


def getPolymer(text):
    lines = text.splitlines()
    template = lines[0]
    pairs = {}
    for i in range(2, len(lines)):
        pair = lines[i].split("->")
        pairs[pair[0].strip()] = pair[1].strip()
    return template, pairs


def polymerize(template, pairs, steps=10):
    polymer = deque(template)
    for i in range(steps):
        j = 1
        while j < len(polymer):
            key = polymer[j - 1] + polymer[j]

            if key in pairs:
                val = pairs[key]
                polymer.insert(j, val)
                j += 2
            else:
                j += 1

    counts = Counter(polymer).values()
    return max(counts) - min(counts)


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
    template, pairs = getPolymer(example)
    assert template == "NNCB"
    assert len(pairs) == 16


Case = namedtuple("Case", ["steps", "expected"])


def test_polymerize_example():
    template, pairs = getPolymer(example)
    cases = [
        Case(10, 1588),
        # Case(40, 2188189693529),
    ]
    for c in cases:
        actual = polymerize(template, pairs, c.steps)
        assert actual == c.expected


# def test_polymerize():
#     template, pairs = getPolymer(getInput())
#     actual = polymerize(template, pairs, 10)
#     assert actual == 2768
