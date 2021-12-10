import utils
from collections import namedtuple
from itertools import permutations


def getInput():
    lines = utils.Inputstr("08")
    return utils.Array(lines)


def easy_digits(segments):
    output_patterns = [l[-4:] for l in segments]
    unique_pattern_lengths = set([2, 3, 4, 7])
    result = 0
    for patterns in output_patterns:
        for p in patterns:
            if len(p) in unique_pattern_lengths:
                result += 1
    return result


VALID_NUMBERS = {
    (True, True, True, False, True, True, True): 0,
    (False, False, True, False, False, True, False): 1,
    (True, False, True, True, True, False, True): 2,
    (True, False, True, True, False, True, True): 3,
    (False, True, True, True, False, True, False): 4,
    (True, True, False, True, False, True, True): 5,
    (True, True, False, True, True, True, True): 6,
    (True, False, True, False, False, True, False): 7,
    (True, True, True, True, True, True, True): 8,
    (True, True, True, True, False, True, True): 9,
}


def decode(signal, wiring):
    for pattern in VALID_NUMBERS:
        result = [False] * 7
        for s in signal:
            i = wiring.index(s)
            result[i] = True
        result = tuple(result)
        if result in VALID_NUMBERS:
            return VALID_NUMBERS[result]
    return None


WIRINGS = ["".join(t) for t in permutations("abcdefg")]


def find_pattern(signals):
    want = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for w in WIRINGS:
        result = set()
        for s in signals:
            number = decode(s, w)
            result.add(number)
        if result == want:
            return w
    return None


def digits(segments):
    total = 0
    for s in segments:
        signals = s[:10]
        outputs = s[-4:]
        p = find_pattern(signals)
        if p:
            result = []
            for o in outputs:
                result.append(decode(o, p))
            total += int("".join([str(val) for val in result]))

    return total


example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


single_example = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""


def test_easy_digits_example():
    lines = utils.Array(example)
    actual = easy_digits(lines)

    assert actual == 26


def test_easy_digits():
    lines = getInput()
    actual = easy_digits(lines)

    assert actual == 456


def test_digits():
    lines = getInput()
    actual = digits(lines)

    assert actual == 1091609


def test_digits_example():
    lines = utils.Array(example)
    actual = digits(lines)

    assert actual == 61229


def test_find_pattern_single_example():
    lines = utils.Array(single_example)
    signals = lines[0][:10]
    actual = find_pattern(signals)

    assert actual == "deafgbc"


def test_digits_single_example():
    lines = utils.Array(single_example)
    actual = digits(lines)

    assert actual == 5353


Case = namedtuple("Case", ["signal", "wiring", "expected"])


def test_decode():
    wiring = "deafgbc"
    cases = [
        Case("acedgfb", wiring, 8),
        Case("cdfbe", wiring, 5),
        Case("gcdfa", wiring, 2),
        Case("fbcad", wiring, 3),
        Case("dab", wiring, 7),
        Case("cefabd", wiring, 9),
        Case("cdfgeb", wiring, 6),
        Case("eafb", wiring, 4),
        Case("cagedb", wiring, 0),
        Case("ab", wiring, 1),
    ]
    for c in cases:
        actual = decode(c.signal, c.wiring)
        assert actual == c.expected
