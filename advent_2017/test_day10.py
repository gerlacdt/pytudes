import day10
import unittest


class TestDay10(unittest.TestCase):
    def test_reverseList(self):
        li = [4,3,0,1,2]
        result = day10.reverse(li, 1, 5)
        expected = [3,4,2,1,0]
        self.assertEqual(result, expected)


    def test_hash_input1(self):
        LENGTHS = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
        ARR = list(range(256))

        result = day10.part1(ARR, LENGTHS)
        expected = 29240
        self.assertEqual(result, expected)


    def test_hash_small_input(self):
        LENGTHS = "3,4,1,5"
        ARR = list(range(5))

        result = day10.part1(ARR, LENGTHS)
        expected = 12
        self.assertEqual(result, expected)
