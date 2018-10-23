from day16 import dance
from myutils import readFile
import unittest


class TestDay16(unittest.TestCase):
    def test_dance(self):
        content = readFile('./data/input16.txt')
        result = dance(content.rstrip("\n"))
        expected = "giadhmkpcnbfjelo"
        self.assertEqual(result, expected)
