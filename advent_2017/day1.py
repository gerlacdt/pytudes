def toList(s):
    return [int(x) for x in s]


def captcha(s):
    digits = toList(s)
    return sum(digits[i] for i in range(len(digits))
               if digits[i] == digits[i-1])


def captcha2(s):
    digits = toList(s)
    steps = int(len(digits) / 2)
    return sum(digits[i] for i in range(len(digits))
               if digits[i-steps] == digits[i])
