from day11 import follow
from myutils import readFile
import unittest


class TestDay11(unittest.TestCase):
    def test_follow(self):
        content = readFile('./data/input11.txt')
        result, maxResult = follow(content)
        expected, maxExpected = 687, 1483
        self.assertEqual(result, expected)
        self.assertEqual(maxResult, maxExpected)
