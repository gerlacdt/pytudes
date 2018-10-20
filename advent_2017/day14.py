# input-(1..n) calculate knot hashes from day10

# convert every char to a 4-char binary string ()

# count all 1s in the binary strings

from functools import reduce
from utils import cat
from day10 import knothash


def toBin(char):
    d = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111',
    }
    return d[char]


def defrag(input1, N=128):
    lines = [knothash("{}-{}".format(input1, i)) for i in range(N)]
    binaryhash = cat([toBin(char) for line in lines for char in line])
    return reduce(lambda acc, c:  acc + 1 if c == '1' else acc, binaryhash, 0)
