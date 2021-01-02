import utils
import re

# from collections import defaultdict


def getInput():
    return utils.Inputstr("04")


def parse(s):
    current = {}
    result = []
    for l in s.splitlines():
        if not l:
            result.append(current)
            current = {}
            continue
        for word in l.split():
            key, value = word.split(":")
            current[key] = value
    return result


def isValid(passport):
    keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    for k in keys:
        if k not in passport:
            return False
    return True


def isValid2(passport):
    keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    for k in keys:
        if k not in passport:
            return False
        val = passport[k]
        if k == "byr":
            ival = int(val)
            if ival >= 1920 and ival <= 2002:
                continue
            else:
                return False
        elif k == "iyr":
            ival = int(val)
            if ival >= 2010 and ival <= 2020:
                continue
            else:
                return False
        elif k == "eyr":
            ival = int(val)
            if ival >= 2020 and ival <= 2030:
                continue
            else:
                return False
        elif k == "hgt":
            m = re.match("^([1-9][0-9]+)(cm|in)$", val)
            if not m:
                return False
            v = int(m.group(1))
            unit = m.group(2)
            if unit == "cm" and v >= 150 and v <= 193:
                continue
            elif unit == "in" and v >= 59 and v <= 76:
                continue
            else:
                return False
        elif k == "hcl":
            if re.match("^#[0-9a-f]{6}$", val):
                continue
            else:
                return False
        elif k == "ecl":
            colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            if val in colors:
                continue
            else:
                return False
        elif k == "pid":
            if re.match("^[0-9]{9}$", val):
                continue
            else:
                return False
    return True


def validate(passports, fn):
    return len(list(filter(fn, passports)))


def testValidate():
    #     s = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    # byr:1937 iyr:2017 cid:147 hgt:183cm

    # iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    # hcl:#cfa07d byr:1929

    # hcl:#ae17e1 iyr:2013
    # eyr:2024
    # ecl:brn pid:760753108 byr:1931
    # hgt:179cm

    # hcl:#cfa07d eyr:2025 pid:166559648
    # iyr:2011 ecl:brn hgt:59in
    # """

    s = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

"""

    passports = parse(s)
    actual = validate(passports, isValid2)
    expected = 1
    assert actual == expected


def testPart1():
    actual = validate(parse(getInput()), isValid)
    expected = 256
    assert actual == expected


def testPart2():
    actual = validate(parse(getInput()), isValid2)
    expected = 198
    assert actual == expected
