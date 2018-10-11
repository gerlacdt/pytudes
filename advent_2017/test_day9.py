import day9
import myutils
import unittest


class TestDay9(unittest.TestCase):
    def test_part1(self):
        input1 = myutils.readFile('./data/input9.txt')
        result1, result2 = day9.part1(input1)
        expected1 = 10800
        expected2 = 4522

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
