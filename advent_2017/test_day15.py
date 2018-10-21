from day15 import judge
import unittest


class TestDay15(unittest.TestCase):
    def test_judge(self):
        genA = 591
        genB = 393
        result = judge(genA, genB, N=40000000)
        expected = 619
        self.assertEqual(result, expected)
