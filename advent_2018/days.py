import operator
from utils import Array, Integers, mapt, Inputstr, cat
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


def day3_part12():
    lines = Inputstr(3).splitlines()
    markedPositions = defaultdict(int)
    claims = []
    for line in lines:
        id, _ , pos, area = line.split(" ")
        pos, area = Integers(pos), Integers(area.replace("x", ","))
        claims.append((id, pos, area))
        x, y = pos
        xs, ys = area
        for i in range(xs):
            for j in range(ys):
                newpos = (x+i, y+j)
                markedPositions[newpos] += 1

    overlaps = len({k: v for k, v in markedPositions.items() if v > 1})

    # find no overlapping claim
    for c in claims:
        id, pos, area = c
        x, y = pos
        xs, ys = area
        no_overlap = all([markedPositions[(x+i, y+j)] == 1
                          for i in range(xs)
                          for j in range(ys)])
        if no_overlap:
            return overlaps, int(id[1:])
    return None


# day4


day4_test_input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""

input4 = Inputstr(4)


def day4_sleep_schedule(content):
    lines = sorted(content.splitlines())
    current_guard = None
    current_date = None
    start_sleeping = 999
    sleep_schedule = defaultdict(dict)
    # collect all sleeping time for a guard from 00:00 to 00:59
    for line in lines:
        if "Guard" in line:
            date, time, _, guard_id, *rest = line.split()
            date = date[1:]
            hour, minute = (int(x) for x in time[:-1].split(":"))
            if hour != 0:
                year, month, day = date.split("-")
                day = int(day) + 1
                date = "{}-{}-{:02d}".format(year, month, day)
            start_sleeping = 999
            current_date = date
            current_guard = int(guard_id[1:])
            if not sleep_schedule[current_guard]:
                sleep_schedule[current_guard] = {}
            sleep_schedule[current_guard][current_date] = [0] * 59
        elif "asleep" in line:
            date, time, *rest = line.split()
            hour, minute = (int(x) for x in time[:-1].split(":"))
            start_sleeping = minute
        elif "wakes" in line:
            date, time, *rest = line.split()
            hour, minute = (int(x) for x in time[:-1].split(":"))
            sleep_schedule[current_guard][current_date][start_sleeping:minute] = [1] * (minute - start_sleeping)
        else:
            raise RuntimeError("error in input line: {}".format(line))
    return sleep_schedule


def day4_part1(content=input4):
    sleep_schedule = day4_sleep_schedule(content)
    guards = {}
    for guard, days in sleep_schedule.items():
        guards[guard] = sum([Counter(schedule)[1] for schedule in days.values()])

    max_guard = max(guards.items(), key=operator.itemgetter(1))[0]

    # count frequency of sleeping minutes from 0 to 59 for all days of
    # the most sleeping guard
    minutes = [day for day in sleep_schedule[max_guard].values()]

    zipped = list(zip(*minutes))
    ranked = [sum(t) for t in zipped]

    return max_guard * ranked.index(max(ranked))


def day4_part2(content=input4):
    sleep_schedule = day4_sleep_schedule(content)

    max_sleep_minutes = {}
    for guard, days in sleep_schedule.items():
        minutes = [day for day in days.values()]
        zipped = list(zip(*minutes))
        ranked = [sum(t) for t in zipped]
        max_sleep_minutes[guard] = ranked.index(max(ranked))

    result = max(max_sleep_minutes.items(), key=operator.itemgetter(1))
    return result[0] * result[1]


# day 5


day5_test_input = "dabAcCaCBAcCcaDA"  # expected result is 10 units


def day5_part1(content=day5_test_input):
    return None
