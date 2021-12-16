import utils

from collections import Counter, namedtuple, defaultdict


def getInput():
    return utils.Inputstr("14")


def parse(text):
    lines = text.splitlines()
    template = lines[0]
    rules = {}
    for i in range(2, len(lines)):
        pair = lines[i].split("->")
        rules[pair[0].strip()] = pair[1].strip()
    return template, rules


def step(pair_counts, element_counts, rules):
    pair_result = defaultdict(int)
    element_result = element_counts.copy()
    for key, insert_element in rules.items():
        element_result[insert_element] += pair_counts[key]
        pair_result[key[0] + insert_element] += pair_counts[key]
        pair_result[insert_element + key[1]] += pair_counts[key]
    return pair_result, element_result


def polymerize(template, rules, steps=10):
    pair_counts = defaultdict(int)
    element_counts = Counter(template)

    # create pair counts from initial polymer
    for i in range(1, len(template)):
        pair_counts[template[i - 1] + template[i]] += 1

    # execute steps
    for i in range(steps):
        pair_counts, element_counts = step(pair_counts, element_counts, rules)
    return max(element_counts.values()) - min(element_counts.values())


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


def test_parse():
    template, rules = parse(example)
    assert template == "NNCB"
    assert len(rules) == 16


Case = namedtuple(
    "Case",
    ["steps", "expected"],
)


def test_polymerize_example():
    template, rules = parse(example)
    cases = [
        Case(1, 1),
        Case(2, 5),
        Case(3, 7),
        Case(4, 18),
        Case(10, 1588),
        Case(40, 2188189693529),
    ]
    for c in cases:
        actual = polymerize(template, rules, c.steps)
        assert actual == c.expected, "Case: {}".format(c)


def test_polymerize():
    template, rules = parse(getInput())
    cases = [Case(10, 2768), Case(40, 2914365137499)]

    for c in cases:
        actual = polymerize(template, rules, c.steps)
        assert actual == c.expected, "Case: steps: {}".format(c.steps)
