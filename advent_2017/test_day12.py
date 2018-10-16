from day12 import part1, part2
from myutils import readFile
import unittest


class TestDay12(unittest.TestCase):
    def test_part1(self):
        content = readFile('./data/input12.txt')
        result = part1(content)
        expected = 288
        self.assertEqual(result, expected)

    def test_part2(self):
        content = readFile('./data/input12.txt')
        result = part2(content)
        expected = 211
        self.assertEqual(result, expected)
