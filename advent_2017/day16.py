from utils import cat, cache


def parse(input1):
    commands = input1.split(",")
    return commands


@cache
def execute(command, progs):
    """Execute given command on programs. sX rotates X to the left"""
    c = command[0]
    result = ""
    if c == 's':
        steps = int(command[1:])
        result = progs[-steps:] + progs[:-steps]
        return result
    elif c == 'x':
        cs = command[1:].split('/')
        i = int(cs[0])
        j = int(cs[1])
        s = list(progs)
        s[i], s[j] = s[j], s[i]
        return cat(s)
    elif c == 'p':
        cs = command[1:].split("/")
        i = int(progs.find(cs[0]))
        j = int(progs.find(cs[1]))
        s = list(progs)
        s[i], s[j] = s[j], s[i]
        return cat(s)
    raise RuntimeError("Given command does not exist: {}".format(command))


PROGRAMS = "abcdefghijklmnop"


def dance(input1, programs=PROGRAMS, N=1):
    commands = parse(input1)
    progs = programs
    for i in range(N):
        for j, c in enumerate(commands):
            progs = execute(c, progs)
    return progs


def whole_dance(input1, programs=PROGRAMS, N=10**9):
    """Idea for N = one billion: Observation every 36 iterations the
start-input re-appears. Hence we can use the following formula:
N % 36 runs are needed. For 1 billion 28 runs.
    """
    commands = parse(input1)
    progs = programs

    for i in range(N % 36):
        for j, c in enumerate(commands):
            progs = execute(c, progs)
    return progs
