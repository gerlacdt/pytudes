from ceasar import guess, encode, decode, createWordTable
import unittest


class TestCesar(unittest.TestCase):
    def test_guess(self):
        wordTable = createWordTable()
        texts = ["danger has come", "with new line\n and period. And comma"]
        testtable = [(encode(text, i), (decode(encode(text, i), i)))
                     for text in texts for i in range(26)]

        for case in testtable:
            input1 = case[0]
            result = guess(input1, wordTable)
            expected = case[1]
            self.assertEqual(result, expected)
