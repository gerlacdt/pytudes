from collections import Counter


def readFile(filename):
    '''Read whole file with filename into a string and returns it.'''
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content


def isValid(s, anagram=False):
    '''Accepts a long string with multiple lines and checks how many lines
are valid passphrases. A passphrase/line is valid if a line does not
contain duplicate words.
    '''
    return len([line for line in s.splitlines() if noDuplicate(line, anagram)])


def noDuplicate(line, anagram=False):
    words = line.split()
    if anagram:
        words = [''.join(sorted(w)) for w in words]
    counts = Counter(words)
    return all([value == 1 for key, value in counts.items()])
