from utils import cat

input1 = "s1,x3/4,pe/b"
input2 = "s1,x14/15,pe/b"


def parse(input1):
    commands = input1.split(",")
    return commands


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


def dance(input1, programs=PROGRAMS):
    commands = parse(input1)
    progs = programs
    for c in commands:
        progs = execute(c, progs)
    return progs
