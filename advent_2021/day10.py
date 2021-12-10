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
