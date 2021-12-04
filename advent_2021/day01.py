import utils


def getInput():
    return utils.Integers(utils.Inputstr("01"))


def sonar(depths):
    counter = 0
    prev = depths[0]
    for i in range(1, len(depths)):
        val = depths[i]
        if val > prev:
            counter += 1
        prev = val
    return counter


def sonarSlidingWindow(depths):
    triples = []
    for i in range(2, len(depths)):
        val = depths[i - 2] + depths[i - 1] + depths[i]
        triples.append(val)
    return sonar(triples)


def test1():
    depths = getInput()
    actual = sonar(depths)
    assert actual == 1715


def test2():
    depths = getInput()
    actual = sonarSlidingWindow(depths)
    assert actual == 1739


def test2_example():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = sonarSlidingWindow(depths)
    assert actual == 5
