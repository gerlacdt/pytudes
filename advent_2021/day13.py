import utils


def getInput():
    return utils.Inputstr("13")


def printDots(dots):
    maxX = max(dot[0] for dot in dots)
    maxY = max(dot[1] for dot in dots)
    dots = set(dots)

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    return None


def getDotsFolds(text):
    lines = utils.Array(text)
    index = lines.index(())
    dots = lines[:index]
    folds = lines[index + 1 :]
    return dots, folds


AXIS_X = "X"
AXIS_Y = "Y"


def getFold(foldTuple):
    """Given instructions from given tuple ('fold', 'along', 'x=5'), return ('x',5)"""
    instruction = foldTuple[-1]
    direction, val = instruction.split("=")
    if direction == "y":
        return int(val), AXIS_Y
    return int(val), AXIS_X


def mirror(dot, fold, maxPoint):
    x, y = dot
    fold_val = fold[0]
    if fold[1] == AXIS_Y:
        # mirror down -> up
        distance = abs(y - fold_val)
        new_y = fold_val - distance
        return (x, new_y)
    else:
        # mirror right -> left
        distance = abs(x - fold_val)
        new_x = fold_val - distance
        return (new_x, y)


def single_fold(dots, fold):
    result = set()
    fold = getFold(fold)
    maxX = max(dot[0] for dot in dots)
    maxY = max(dot[1] for dot in dots)
    maxPoint = (maxX, maxY)

    for dot in dots:
        x, y = dot
        # mirror dots
        if fold[1] == AXIS_Y:
            if y < fold[0]:
                # dot stays the same
                result.add(dot)
            else:
                # mirror dot
                mirror_dot = mirror(dot, fold, maxPoint)
                # print("dot: {} mirror: {}".format(dot, mirror_dot))
                result.add(mirror_dot)
        else:
            if x < fold[0]:
                # dot stays the same
                result.add(dot)
            else:
                # mirror dot
                mirror_dot = mirror(dot, fold, maxPoint)
                result.add(mirror_dot)

    return result


def fold(dots, folds):
    current_dots = dots
    for fold in folds:
        current_dots = single_fold(current_dots, fold)

    printDots(current_dots)


example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_getFold():
    _, folds = getDotsFolds(example)
    actual = getFold(folds[0])
    assert actual == (7, "Y")


def test_single_fold_example():
    dots, folds = getDotsFolds(example)
    actual = single_fold(dots, folds[0])
    assert len(actual) == 17


def test_single_fold():
    dots, folds = getDotsFolds(getInput())
    actual = single_fold(dots, folds[0])
    assert len(actual) == 729


def test_fold_example():
    dots, folds = getDotsFolds(example)
    actual = fold(dots, folds)
    assert 1 == 0  # fail to see STDOUT


def test_fold():
    dots, folds = getDotsFolds(getInput())
    actual = fold(dots, folds)
    assert 1 == 0  # fail to see STDOUT

    # result code: RGZLBHFP
