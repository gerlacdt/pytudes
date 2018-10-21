def judge(startA, startB, factorA=16807, factorB=48271, N=5):
    genA = gen(startA, factorA)
    genB = gen(startB, factorB)
    acc = 0
    for i in range(N):
        valA = next(genA)
        valB = next(genB)
        binA = toBin(valA)
        binB = toBin(valB)
        if binA[16:] == binB[16:]:
            acc += 1
    return acc


def gen(start, factor):
    divider = 2147483647
    val = start
    while True:
        t = val * factor
        val = t % divider
        yield val


def toBin(n):
    return "{0:032b}".format(n)
