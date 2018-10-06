from collections import Counter
from myutils import readFile


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
