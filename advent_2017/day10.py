from utils import grouper, cat
from functools import reduce
from operator import xor


def part1(stream, N=256):
    arr = list(range(N))
    lengths = map(int, stream.split(','))
    currentIndex = skipsize = 0

    for l in lengths:
        arr = reverse(arr, currentIndex, l)
        currentIndex = (currentIndex + l + skipsize) % len(arr)
        skipsize += 1

    return arr[0] * arr[1]


def reverse(nums, pos, L):
    '''Norvig Solution: Reverse nums[pos:pos+L], handling wrap-around.
    '''
    # Move first pos elements to end, reverse first L, move pos elements back
    nums = nums[pos:] + nums[:pos]
    nums[:L] = reversed(nums[:L])
    nums = nums[-pos:] + nums[:-pos]
    return nums


def part2(stream, N=256, rounds=64, suffix=[17, 31, 73, 47, 23]):
    arr = list(range(N))
    lengths = [ord(c) for c in stream]
    lengths += suffix

    skipsize = currentIndex = 0

    for i in range(rounds):
        for l in lengths:
            arr = reverse(arr, currentIndex, l)
            currentIndex = (currentIndex + l + skipsize) % len(arr)
            skipsize += 1

    # dense hash
    chunks = list(grouper(arr, 16))
    xorChunks = [reduce(lambda x, y: xor(x, y), chunk) for chunk in chunks]

    return cat(map(lambda item: "{:02x}".format(item), xorChunks))
