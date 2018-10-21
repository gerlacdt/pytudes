from numba import jit


def judge(startA, startB, factorA=16807, factorB=48271, multipliesA=1,
          multipliesB=1, N=5):
    genA = gen(startA, factorA, multipliesA)
    genB = gen(startB, factorB, multipliesB)
    mask = 2**16-1
    acc = 0
    for i in range(N):
        valA = next(genA)
        valB = next(genB)
        if valA & mask == valB & mask:
            acc += 1
    return acc


def gen(start, factor, multiplies=1):
    divider = 2147483647
    val = start
    while True:
        t = val * factor
        val = t % divider
        if val % multiplies == 0:
            yield val


@jit
def duelgen(prev1=591, factor1=16807, prev2=393, factor2=48271,
            m=2147483647, mask=2**16-1, N=40*10**6):
    """numba.jit does not work with generators. So this is the rewrite
from part 1."""
    matches = 0
    for _ in range(N):
        prev1 = (prev1 * factor1) % m
        prev2 = (prev2 * factor2) % m
        matches += (prev1 & mask == prev2 & mask)
    return matches
