from collections import Counter
from myutils import readFile

letters = "abcdefghijklmnopqrstuvwxyz"
lettersLength = len(letters)


def getWords(content):
    lines = content.splitlines()
    return [word.rstrip(',.-') for line in lines
            for word in line.split() if word.rstrip(',.-').isalpha()]


def createWordTable(filename='big.txt'):
    content = readFile(filename)
    words = getWords(content)
    return Counter(words)


def guess(ciphertext, wordTable):
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
    return ''.join([letters[(letters.index(char.lower()) + n) % lettersLength]
                    if char.isalpha() else char
                    for idx, char in enumerate(string)])


def encode(plaintext, n):
    return rotate(plaintext, n)


def decode(ciphertext, n):
    return rotate(ciphertext, -n)
