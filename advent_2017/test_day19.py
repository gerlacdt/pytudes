from day19 import tubes
from myutils import readFile
import unittest


class TestDay19(unittest.TestCase):
    def test_tubes(self):
        input1 = readFile("./data/input19.txt")
        result = tubes(input1)
        expected = ("AYRPVMEGQ", 16408)
        self.assertEqual(result, expected)
