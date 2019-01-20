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


def process2(data):
    def helper():
        nchildren, nmetadata = data.popleft(), data.popleft()
        if nchildren == 0:
            value = 0
            for n in range(nmetadata):
                value += data.popleft()
            return value
        else:
            child_values = []
            for c in range(nchildren):
                child_values.append(helper())
            value = 0
            for n in range(nmetadata):
                metadata = data.popleft()
                if metadata-1 < nchildren:
                    value += child_values[metadata-1]
            return value
    return helper()


def solve2(content=test_input):
    data = deque([int(s) for s in content.split(" ")])
    metadata = process2(data)
    return metadata
