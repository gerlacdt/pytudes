def judge(startA, startB, factorA=16807, factorB=48271, multipliesA=1,
          multipliesB=1, N=5):
    genA = gen(startA, factorA, multipliesA)
    genB = gen(startB, factorB, multipliesB)
    acc = 0
    for i in range(N):
        valA = next(genA)
        valB = next(genB)
        binA = toBin(valA)
        binB = toBin(valB)
        if binA[16:] == binB[16:]:
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


def toBin(n):
    return "{0:032b}".format(n)
