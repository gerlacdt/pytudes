def readBanks(content):
    lines = content.splitlines()
    return [int(word) for line in lines for word in line.split()]


def mem_realloc(banks):
    length = len(banks)
    duplicates = {}
    steps = 0

    while True:
        duplicates[(tuple(banks))] = steps
        steps += 1
        maxVal = max(banks)
        maxIdx = banks.index(maxVal)

        banks[maxIdx] = 0
        for i in range(1, maxVal+1):
            banks[(maxIdx + i) % length] += 1
        if tuple(banks) in duplicates:
            cycles = steps - duplicates[tuple(banks)]
            break
    return steps, cycles
