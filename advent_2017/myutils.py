from itertools import islice


def readFile(filename):
    '''Read whole file with filename into a string and returns it.'''
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
