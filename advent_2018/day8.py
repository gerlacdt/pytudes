from collections import deque
from utils import Inputstr

test_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


def process(data):
    metadata = 0

    def helper():
        # recursive function
        nonlocal metadata
        nchildren, nmetadata = data.popleft(), data.popleft()
        for c in range(nchildren):
            helper()
        for n in range(nmetadata):
            metadata += data.popleft()
    helper()
    return metadata


input8 = Inputstr(8)


def solve1(content=test_input):
    data = deque([int(s) for s in content.split(" ")])
    metadata = process(data)
    return metadata
