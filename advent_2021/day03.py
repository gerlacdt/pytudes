import utils


def getInput():
    return utils.Inputstr("03").splitlines()


def toInt(arr):
    """Returns an integer from a binary representation, arr is a list of
    0s and 1s. E.g. ['1', '0', '0']"""
    return int("".join(arr), 2)


def power_consumtion(positions):
    transposed = list(zip(*positions))
    gamma = []
    epsilon = []
    for line in transposed:
        ones = line.count("1")
        zeros = line.count("0")
        if ones > zeros:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    return toInt(gamma) * toInt(epsilon)


def life_support_rating(positions):
    def mostCommon(ones, zeros):
        return "1" if ones >= zeros else "0"

    def leastCommon(ones, zeros):
        return "0" if zeros <= ones else "1"

    def calculate(positions, commonFilter):
        current = positions
        index = 0
        while len(current) > 1:
            transposed = list(zip(*current))
            ones = transposed[index].count("1")
            zeros = transposed[index].count("0")
            common = commonFilter(ones, zeros)
            current = [val for val in current if val[index] == common]
            index += 1
        return toInt(current[0])

    oxygen = calculate(positions, mostCommon)
    co2 = calculate(positions, leastCommon)

    return oxygen * co2


def test_power_consumtion():
    actual = power_consumtion(getInput())
    expected = 1082324

    assert actual == expected


example_positions = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_power_consumtion_example():

    actual = power_consumtion(example_positions)
    expected = 198

    assert actual == expected


def test_life_support_rating_example():
    actual = life_support_rating(example_positions)
    expected = 230

    assert actual == expected


def test_life_support_rating():
    actual = life_support_rating(getInput())
    expected = 1353024

    assert actual == expected
