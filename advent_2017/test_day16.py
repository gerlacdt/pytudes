from day16 import dance, whole_dance
from myutils import readFile
import unittest


class TestDay16(unittest.TestCase):
    def test_dance(self):
        content = readFile('./data/input16.txt')
        result = dance(content.rstrip("\n"))
        expected = "giadhmkpcnbfjelo"
        self.assertEqual(result, expected)

    def test_dance_2(self):
        content = readFile('./data/input16.txt')
        result = whole_dance(content.rstrip("\n"))
        expected = "njfgilbkcoemhpad"
        self.assertEqual(result, expected)
