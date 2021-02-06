import utils

from collections import defaultdict
from functools import lru_cache


def getInput():
    return list(utils.Integers(utils.Inputstr("10")))


def calcJolts(jolts):
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    diffs = defaultdict(int)
    if jolts[0] > 3:
        raise RuntimeError(f"Invalid start jolt: {jolts[0]}")
    diffs[jolts[0]] = 1
    for i in range(1, len(jolts)):
        prev = jolts[i - 1]
        curr = jolts[i]
        diff = curr - prev
        if diff > 3:
            raise RuntimeError(
                f"Invalid jolt, not compatible: prev: {jolts[i-1]} <> {jolts[i]}"
            )
        diffs[diff] += 1
    return diffs[1] * diffs[3]


def day10_2(jolts):
    return arrangements(tuple(sorted(jolts)), 0)


@lru_cache(None)
def arrangements(jolts, prev) -> int:
    "The number of arrangements that go from prev to the end of `jolts`."
    first, rest = jolts[0], jolts[1:]
    if first - prev > 3:
        return 0
    elif not rest:
        return 1
    else:
        return arrangements(rest, first) + arrangements(  # Use first
            rest, prev
        )  # Skip first


assert arrangements((3, 6, 9, 12), 0) == 1
assert arrangements((3, 6, 9, 13), 0) == 0
assert arrangements((1, 2, 3, 4), 0) == 7


ex1 = """16
10
15
5
1
11
7
19
6
12
4
"""

ex2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def testExample1():
    jolts = list(utils.Integers(ex1))
    actual = calcJolts(jolts)
    expected = 35
    assert actual == expected

    jolts = list(utils.Integers(ex2))
    actual = calcJolts(jolts)
    expected = 220
    assert actual == expected


def testExample2():
    jolts = list(utils.Integers(ex1))
    actual = day10_2(jolts)
    expected = 8
    assert actual == expected

    jolts = list(utils.Integers(ex2))
    actual = day10_2(jolts)
    expected = 19208
    assert actual == expected


def testJolts():
    actual = calcJolts(getInput())
    expected = 2210
    assert actual == expected


def testArrangements():
    actual = day10_2(getInput())
    expected = 7086739046912
    assert actual == expected
