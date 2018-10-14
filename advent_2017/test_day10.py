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

        result = day10.part1(LENGTHS)
        expected = 29240
        self.assertEqual(result, expected)

    def test_hash_small_input(self):
        LENGTHS = "3,4,1,5"

        result = day10.part1(LENGTHS, N=5)
        expected = 12
        self.assertEqual(result, expected)

    def test_hash_part2(self):
        tests = {
            "": "a2582a3a0e66e6e86e3812dcb672a272",
            "AoC 2017": "33efeb34ea91902bb2f59c9920caa6cd",
            "1,2,3": "3efbe78a8d82f29979031a4aa0b16a9d",
            "1,2,4": "63960835bcdc130f0b66d7ff4f6a5a8e",
            "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229": "4db3799145278dc9f73dcdbc680bd53d",
        }

        for input1, expected in tests.items():
            result = day10.part2(input1)
            self.assertEqual(result, expected, "{} failed".format(input1))
