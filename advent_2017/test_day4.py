import day4
import unittest


class TestDay4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        filename = 'data/input4.txt'
        cls.content = day4.readFile(filename)

    def test_passphrase(self):
        result = day4.isValid(self.content)
        expected = 383
        self.assertEqual(result, expected)

    def test_passphrase_anagram(self):
#         content = '''abcde fghij
# abcde xyz ecdab
# a ab abc abd abf abj
# iiii oiii ooii oooi oooo
# oiii ioii iioi iiio
# '''
        result = day4.isValid(self.content, True)
        expected = 265
        self.assertEqual(result, expected)
