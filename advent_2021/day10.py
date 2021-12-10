import utils


def getInput():
    lines = utils.Inputstr("10")
    return (t[0] for t in utils.Array(lines))


ERROR_TABLE = {")": 3, "]": 57, "}": 1197, ">": 25137}
OPENING = set(["(", "[", "{", "<"])
MATCHING = {")": "(", "]": "[", "}": "{", ">": "<"}


def check_syntax(chunks):
    error_score = 0
    for chunk in chunks:
        stack = []
        for char in chunk:
            if char in OPENING:
                stack.append(char)
            else:
                if MATCHING[char] == stack[-1]:
                    stack.pop()
                else:
                    error_score += ERROR_TABLE[char]
                    break
    return error_score


# part 2


def is_corrupt(chunk):
    stack = []
    for char in chunk:
        if char in OPENING:
            stack.append(char)
        else:
            if MATCHING[char] == stack[-1]:
                stack.pop()
            else:
                return True
    return False


def is_complete(chunk):
    stack = []
    for char in chunk:
        if char in OPENING:
            stack.append(char)
        else:
            if MATCHING[char] == stack[-1]:
                stack.pop()
    return True if not stack else False


INCOMPLETE_SCORE_TABLE = {"(": 1, "[": 2, "{": 3, "<": 4}


def check_incomplete(chunks):
    # remove corrupt and complete lines
    chunks = filter(lambda x: not is_corrupt(x), chunks)
    chunks = filter(lambda x: not is_complete(x), chunks)

    # complete chunks
    current_scores = []
    for chunk in chunks:
        stack = []
        for char in chunk:
            if char in OPENING:
                stack.append(char)
            else:
                if MATCHING[char] == stack[-1]:
                    stack.pop()

        # calculate score for single chunk
        current_score = 0
        while stack:
            char = stack.pop()
            current_score *= 5
            current_score += INCOMPLETE_SCORE_TABLE[char]
        current_scores.append(current_score)

    mid = len(current_scores) // 2
    current_scores.sort()
    return current_scores[mid]


example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

single_line = "[<(<(<(<{}))><([]([]()"


def test_check_syntax_example():
    chunks = (t[0] for t in utils.Array(example))
    actual = check_syntax(chunks)
    assert actual == 26397


def test_check_syntax():
    chunks = (t[0] for t in utils.Array(getInput()))
    actual = check_syntax(chunks)
    assert actual == 392367


def test_check_incomplete():
    chunks = (t[0] for t in utils.Array(example))
    actual = check_incomplete(chunks)
    assert actual == 288957


def test_check_incomplete():
    chunks = (t[0] for t in utils.Array(getInput()))
    actual = check_incomplete(chunks)
    assert actual == 2192104158
