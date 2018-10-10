import day8
import myutils
import unittest


class TestDay8(unittest.TestCase):
    def test_part1(self):
        input1 = myutils.readFile('./data/input8.txt')
        result1, result2 = day8.part12(input1)
        expected1, expected2 = 4832, 5443

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
