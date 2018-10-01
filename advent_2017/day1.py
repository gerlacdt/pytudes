def toList(s):
    return [int(x) for x in s]


def captcha(s):
    digits = toList(s)
    return sum(digits[i] for i in range(len(digits))
               if digits[i] == digits[i-1])
    # seq = seq + [seq[0]]
    # acc = 0
    # for idx, val in enumerate(seq):
    #     if idx == len(seq) - 1:
    #         break
    #     if val == seq[idx + 1]:
    #         acc += val
    # return acc
