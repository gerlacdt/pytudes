from utils import Inputstr, cat, rangei, nth, mapt
from itertools import islice


test = """#..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""


def Plants(row):
    "Convert '#..#.#' => {0, 3, 5}"
    return {i for i, c in enumerate(row) if c == '#'}


def grow(plants, rules):
    "Grow plants using rules, yielding each generation (including 0th)."
    while True:
        yield plants
        extent = rangei(min(plants) - 3, max(plants) + 3)
        plants = {i for i in extent if lives(plants, i, rules)}


def lives(plants, i, rules):
    "Does pot i live in next generation, according to rules?"
    neighborhood = cat('.#'[j in plants] for j in rangei(i - 2, i + 2))
    return rules.get(neighborhood) == '#'


input12 = Inputstr(12)


def part1(content=input12):
    input1 = mapt(str.split, content.splitlines())
    plants  = Plants(input1[0][-1])
    rules   = {rule[0]: rule[-1] for rule in input1 if '=>' in rule}
    return sum(nth(grow(plants, rules), 20))


def part2(content=input12):
    input1 = mapt(str.split, content.splitlines())
    plants  = Plants(input1[0][-1])
    rules   = {rule[0]: rule[-1] for rule in input1 if '=>' in rule}

    def nth_plant_sum(n, k=190):
        "The sum of plants in the nth generation, assuming linear growth after k generations."
        a, b = map(sum, islice(grow(plants, rules), k, k + 2))
        return a + (n - k) * (b - a)

    return nth_plant_sum(50 * 10 ** 9)  # 50 billion iterations
