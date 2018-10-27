from day18 import duet
from myutils import readFile
import unittest


class TestDay18(unittest.TestCase):
    def test_duet(self):
        input1 = readFile("./data/input18.txt")
        result = duet(input1)
        expected = ('b', 8600)
        self.assertEqual(result, expected)
