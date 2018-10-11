import re


def part1(s):
    # remove ignore chars
    input1 = re.sub("!.", "", s)

    # remove garbage
    input2 = re.sub("<.*?>", "", input1)

    # needed for counting garbage
    input3 = re.sub("<.*?>", "<>", input1)

    # count group scores
    score = 0
    agg = 0
    for c in input2:
        if c == "{":
            score += 1
        elif c == "}":
            agg += score
            score -= 1

    removedGarbage = len(input1) - len(input3)
    return agg, removedGarbage
