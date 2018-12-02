from utils import Integers, mapt, Inputstr, cat
from collections import defaultdict, Counter


def day1_part1():
    lines = Inputstr(1).splitlines()
    numbers = mapt(lambda t: t[0], [Integers(line) for line in lines])
    return sum(numbers)


def day1_part2():
    lines = Inputstr(1).splitlines()
    numbers = mapt(lambda t: t[0], [Integers(line) for line in lines])
    return day1_calc(numbers)


def day1_calc(numbers):
    i = 0
    frequency = 0
    d = defaultdict(int)
    d[0] = 1
    while True:
        n = numbers[i]
        frequency += n
        d[frequency] += 1
        if d[frequency] >= 2:
            break
        if i == len(numbers) - 1:
            i = 0  # reset loop
            continue
        i += 1
    return frequency


def day2_part1():
    lines = Inputstr(2).splitlines()
    duos = 0
    trips = 0
    for line in lines:
        count = Counter(line)
        saw2 = False
        saw3 = False
        print(count)
        for v in count.values():
            if v == 2 and not saw2:
                duos += 1
                saw2 = True
            elif v == 3 and not saw3:
                trips += 1
                saw3 = True
    return duos * trips


def day2_part2():
    lines = sorted(Inputstr(2).splitlines())
    for i, l in enumerate(lines):
        for j, l2 in enumerate(lines):
            if i != j:
                ndiff, indices = string_diff(l, l2)
                if ndiff == 1:
                    return cat([c for j, c in enumerate(l)
                                    if j != indices[0]])
    return None


def string_diff(s1, s2):
    if len(s1) != len(s2):
        raise RuntimeError("ERROR given strings have not the same length.")
    difference = 0
    indices = []
    for i, c in enumerate(s1):
        if s1[i] != s2[i]:
            difference += 1
            indices.append(i)
    return difference, indices
