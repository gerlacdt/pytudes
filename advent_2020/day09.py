import utils


def getInput():
    return [int(line) for line in utils.Inputstr("09").splitlines()]


def twoSum(nums, k):
    cache = {}
    for i, n in enumerate(nums):
        if k - n in cache:
            return [k - n, n]
        cache[n] = i

    return None


def encodingError(instructions, preamble=25):

    for i in range(preamble, len(instructions)):
        val = instructions[i]
        # check if val is correct
        if not twoSum(instructions[i - preamble : i], val):
            return val
    return None


def breakEnc(instructions, result):
    for i in range(len(instructions)):
        current = [instructions[i]]
        for j in range(i + 1, len(instructions)):
            current.append(instructions[j])
            if sum(current) == result:
                return min(current) + max(current)
    return None


example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def testExample1():
    instructions = [int(line) for line in example.splitlines()]
    actual = encodingError(instructions, 5)
    expected = 127
    assert actual == expected


def testExample2():
    instructions = [int(line) for line in example.splitlines()]
    actual = breakEnc(instructions, 127)
    print(actual)
    expected = 62
    assert actual == expected


def testTwoSum():
    nums = [1, 2, 3, 4, 5, 6]
    k = 10
    actual = twoSum(nums, k)
    expected = [4, 6]
    assert actual == expected

    nums = [1, 2, 3, 4, 5, -6]
    k = -2
    actual = twoSum(nums, k)
    expected = [4, -6]
    assert actual == expected

    nums = [1, 2, 3, 4, 5, -6]
    k = 12
    actual = twoSum(nums, k)
    expected = None
    assert actual == expected

    nums = [
        35,
        20,
        15,
        25,
        47,
    ]
    k = 40
    actual = twoSum(nums, k)
    expected = [15, 25]
    assert actual == expected


def testPart1():
    actual = encodingError(getInput())
    expected = 1124361034
    assert actual == expected


def testPart2():
    actual = breakEnc(getInput(), 1124361034)
    expected = 0
    assert actual == expected


def testPositive():
    instructions = getInput()
    assert all([instr >= 0 for instr in instructions])
