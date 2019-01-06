test_input = "dabAcCaCBAcCcaDA"  # expected result is 10 units


def react(c1, c2):
    if c1.lower() == c2.lower() and c1 != c2:
        return True
    return False


def part1(content=test_input):
    arr = list(content)
    current = 1
    previous = 0
    while current < len(arr):
        pass
    return None
