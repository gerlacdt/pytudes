import re
import utils


def getInput():
    return utils.Inputstr("07")


def parse(rules):
    graph = {}
    for line in rules.splitlines():
        rules = re.findall(r"(\d)?\s*(\w+) (\w+) bag|bags", line)
        key = rules[0][1:]
        for i in range(1, len(rules)):
            if rules[i] == ("", "no", "other"):
                graph[key] = []
                continue
            if key not in graph:
                graph[key] = []
            graph[key].append(rules[i])
    return graph


def dfs(graph, target=("shiny", "gold")):
    def helper(start, end):
        frontier = [start]
        visited = set()
        while frontier:
            node = frontier.pop()
            if node == end:
                return True
            visited.add(node)
            for child in graph[node]:
                if child[1:] not in visited:
                    frontier.append(child[1:])
        return None

    counter = 0
    for key in graph.keys():
        if helper(key, target) and key != target:
            counter += 1
    return counter


def dfsPart2(graph, start=("shiny", "gold")):
    def helper(node):
        result = 0
        for child in graph[node[1:]]:
            result += int(node[0]) * helper(child)
        return int(node[0]) + result

    return helper((1, start[0], start[1])) - 1


def testExample():
    rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

    actual = dfs(parse(rules))
    expected = 4
    assert actual == expected


def testExample2():
    rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

    actual = dfsPart2(parse(rules))
    expected = 32
    assert actual == expected

    rules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
    actual = dfsPart2(parse(rules))
    expected = 126
    assert actual == expected


def testPart1():
    actual = dfs(parse(getInput()))
    expected = 337
    assert actual == expected


def testPart2():
    actual = dfsPart2(parse(getInput()))
    expected = 50100
    assert actual == expected
