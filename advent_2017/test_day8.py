import day8
import myutils
import unittest


class TestDay8(unittest.TestCase):
    def test_part1(self):
        input1 = myutils.readFile('./data/input8.txt')
        result = day8.part1(input1)
        expected = 4832

        self.assertEqual(result, expected)
