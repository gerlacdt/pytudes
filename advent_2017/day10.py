from utils import grouper
from functools import reduce
from operator import xor


def part1(arr, lengths):
    # arr = list(range(256))
    lengths = map(int, lengths.split(','))
    skipsize = 0  # increase by 1 every iteration
    currentIndex = 0

    for l in lengths:
        arr = reverse(arr, currentIndex, l)
        currentIndex = (currentIndex + l + skipsize) % len(arr)
        skipsize += 1

    return arr[0] * arr[1]


def reverse(li, currentIndex, reverseLength):
    liLength = len(li)
    newIndex = currentIndex + (reverseLength - 1)
    overshootIndex = newIndex - liLength

    if newIndex < liLength:
        li[currentIndex:newIndex+1] = li[currentIndex:newIndex+1][::-1]
    else:
        tmplist = li[currentIndex:] + li[:overshootIndex+1]
        revlist = tmplist[::-1]

        assert len(li[currentIndex:]) == len(revlist[:reverseLength - overshootIndex - 1])
        li[currentIndex:] = revlist[:reverseLength - overshootIndex - 1]

        assert len(li[:overshootIndex + 1]) == len(revlist[reverseLength - overshootIndex - 1:])
        li[:overshootIndex + 1] = revlist[reverseLength - overshootIndex - 1:]
    return li


def part2(arr, lengths):
    # arr = list(range(256))
    lengths = [ord(c) for c in lengths]
    lengths += [17, 31, 73, 47, 23]

    skipsize = 0  # increase by 1 every iteration
    currentIndex = 0

    # loop 64 times the get the sparse hash
    for i in range(64):
        for l in lengths:
            arr = reverse(arr, currentIndex, l)
            currentIndex = (currentIndex + l + skipsize) % len(arr)
            skipsize += 1

    # get dense hash
    chunks = list(grouper(arr, 16, 99999))
    xorChunks = [reduce(lambda x, y: xor(x, y), chunk) for chunk in chunks]

    def toHex(acc, x):
        if x < 16:
            return acc + '0' + hex(x)[2:]
        return acc + hex(x)[2:]

    return reduce(toHex, xorChunks, '')
