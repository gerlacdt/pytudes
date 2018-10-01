def toList(s):
    return [int(x) for x in s]


def captcha(s):
    digits = toList(s)
    return sum(digits[i] for i in range(len(digits))
               if digits[i] == digits[i-1])
