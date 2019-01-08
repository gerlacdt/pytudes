from utils import Inputstr, letters

test_input = "dabAcCaCBAcCcaDA"  # expected result is 10 units


def react(c1, c2):
    if c1.lower() == c2.lower() and c1 != c2:
        return True
    return False


input5 = Inputstr(5)


def chain_slow(arr):
    current = 1
    previous = 0
    while current < len(arr):
        if react(arr[previous], arr[current]):
            arr = arr[:previous] + arr[current+1:]
            previous -= 1
            current -= 1
        else:
            previous += 1
            current += 1
    return len(arr)


def chain(arr):
    arr2 = []
    current = 1
    previous = 0
    for c in arr:
        if react(arr[previous], arr[current]):
            previous += 1
            current += 1
            continue
        arr2.append(c)
        previous += 1
        current += 1
    return len(arr2)


def part1(content=test_input):
    return chain(list(content))


def part2(content=test_input):
    # remove all letter pairs from given input
    minimum = 9999999
    arr = list(content)
    for letter in letters:
        arr2 = []
        for c in arr:
            if c == letter or c == letter.upper():
                continue
            else:
                arr2.append(c)

        # run reaction chain
        result = chain(arr2)
        print("done for letter: {}".format(letter))
        if result < minimum:
            minimum = result

    return minimum
