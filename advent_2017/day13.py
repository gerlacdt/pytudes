from utils import mapt, Integers, first, count_from


def read(content):
    "Return input tuples ((depth, range), ...)"
    return mapt(Integers, content.splitlines())


def trip_severity(scanners):
    "The sum of severities for each time the packet is caught."
    return sum((d * w if caught(d, w) else 0)
               for (d, w) in scanners)


def caught(depth, width):
    "Does the scanner at this depth/width catch the packet?"
    return depth % (2 * (width - 1)) == 0



# part 2

def caught_delay(depth, width, delay=0):
    "Does the scanner at this depth/width catch the packet with this delay?"
    return (depth + delay) % (2 * (width - 1)) == 0

def safe_delay(scanners):
    "Find the first delay such that no scanner catches the packet."
    safe = lambda delay: not any(caught_delay(d, w, delay) for (d, w) in scanners)
    return first(filter(safe, count_from(0)))
