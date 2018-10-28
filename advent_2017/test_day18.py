from day18 import duet, deadlock
from myutils import readFile
import unittest


class TestDay18(unittest.TestCase):
    def test_duet(self):
        input1 = readFile("./data/input18.txt")
        result = duet(input1)
        expected = 8600
        self.assertEqual(result, expected)

    def test_deadlock(self):
        input1 = readFile("./data/input18.txt")
        result = deadlock(input1)
        expected = 7239
        self.assertEqual(result, expected)
