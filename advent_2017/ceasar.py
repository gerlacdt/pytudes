from collections import Counter
from myutils import readFile

letters = "abcdefghijklmnopqrstuvwxyz"
lettersLength = len(letters)


def getWords(content):
    '''Helper for creating word table. Lowercases words and also strip
periods and commas from them. Input is a big string with multiple
lines. Returns an array of words.
    '''
    lines = content.splitlines()
    return [word.rstrip(',.-') for line in lines
            for word in line.split() if word.rstrip(',.-').isalpha()]


def createWordTable(filename='big.txt'):
    '''Creates a word dictionary with words as keys and their number of
occurrences as values. E.g. {floor -> 32, the -> 122}'''
    content = readFile(filename)
    words = getWords(content)
    return Counter(words)


def guess(ciphertext, wordTable):
    '''Trys to decode the given ciphertext. A wordtable is needed as input
in order to calculate probabilities if a calculated output is a valid
one.'''
    cipherlines = ciphertext.splitlines()
    cipherwords = [word for line in cipherlines for word in line.split()]
    neededHits = len(cipherwords) / 2  # 50 % hits means message is deciphered

    # guess for all possible ceasar rotations, pick best guess
    for n in range(0, 26):
        plaintext = decode(ciphertext, n)
        lines = plaintext.splitlines()
        words = [word for line in lines for word in line.split() ]
        # checks word occurrences
        occurrences = 0
        for w in words:
            if w in wordTable:
                occurrences += 1
        if occurrences >= neededHits:
            return plaintext
    return None


def rotate(string, n):
    '''Rotates the given string with n times. Also considers wrap
overs. E.g. if n == 3, a -> d, z -> c. N can be negative too.
    '''
    return ''.join([letters[(letters.index(char.lower()) + n) % lettersLength]
                    if char.isalpha() else char
                    for idx, char in enumerate(string)])


def encode(plaintext, n):
    '''Encode with ceasar cipher algorithm. N is the rotation number.'''
    return rotate(plaintext, n)


def decode(ciphertext, n):
    '''Decodes the given ciphertext. The ceasar algorithm is used with N
as the given rotation number.'''
    return rotate(ciphertext, -n)
