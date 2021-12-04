import utils
from collections import namedtuple

Field = namedtuple("Field", ["val", "marked"])


def getBoard(lines):
    parsedLines = utils.Array(lines)
    randomNums = parsedLines[0]
    boards = []
    current = []
    for i in range(1, len(parsedLines)):
        line = parsedLines[i]
        if not line:
            if current:
                boards.append(current)
            current = []
            continue
        current.append([Field(n, False) for n in line])
    if current:
        boards.append(current)
    return randomNums, boards


def mark(n, board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if n == col.val:
                board[i][j] = Field(col.val, True)
                return True, i, j
    return False, 0, 0


def sumUnmarked(board):
    total = 0
    for row in board:
        total += sum([col.val for col in row if not col.marked])
    return total


def check(board, i, j):
    # check row i
    row = board[i]
    if all([col.marked for col in row]):
        return True

    # check column j
    transposed = list(zip(*board))
    row = transposed[j]
    if all([col.marked for col in row]):
        return True

    return False


def bingo(nums, boards):
    visited = set()
    for n in nums:
        for index, b in enumerate(boards):
            isMarked, i, j = mark(n, b)
            if isMarked:
                isBingo = check(b, i, j)
                if isBingo and index not in visited:
                    visited.add(index)
                    yield n * sumUnmarked(b)


test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def test_getBoard():
    actualNums, actualBoards = getBoard(test_input)
    assert len(actualNums) == 27
    assert len(actualBoards) == 3
    assert actualBoards[1][2] == [Field(n, False) for n in [19, 8, 7, 25, 23]]


def test_bingo_example():
    nums, boards = getBoard(test_input)
    actual = next(bingo(nums, boards))

    expected = 4512  # 188 * 24 (all unmarked in board * current number)
    assert actual == expected


def test_bingo():
    nums, boards = getBoard(utils.Inputstr("04"))
    actual = next(bingo(nums, boards))

    expected = 64084
    assert actual == expected


def test_bingo_final_example():
    nums, boards = getBoard(test_input)
    for result in bingo(nums, boards):
        actual = result

    expected = 1924
    assert actual == expected


def test_bingo_final():
    nums, boards = getBoard(utils.Inputstr("04"))
    for result in bingo(nums, boards):
        actual = result

    expected = 12833
    assert actual == expected
