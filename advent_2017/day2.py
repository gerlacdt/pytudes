import utils


def checksum(s):
    lines = [line for line in s.split('\n') if line != '']
    arr = map(lambda line: list(map(lambda x: int(x), line.split())), lines)
    return sum([abs(max(line) - min(line)) for line in arr])


def norvig_checksum(rows):
    rows2 = utils.Array(rows)
    return sum(abs(max(row) - min(row)) for row in rows2)


def checksum2(rows):
    rows2 = utils.Array(rows)
    return sum([int(x / y) for row in rows2
                for i, x in enumerate(row)
                for j, y in enumerate(row)
                if i != j and x % y == 0])
