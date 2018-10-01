def toList(s):
    return [int(x) for x in s]


def captcha(s):
    seq = toList(s)
    seq = seq + [seq[0]]
    acc = 0
    for idx, val in enumerate(seq):
        if idx == len(seq) - 1:
            break
        if val == seq[idx + 1]:
            acc += val
    return acc
