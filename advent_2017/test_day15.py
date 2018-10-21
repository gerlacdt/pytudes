from day15 import judge, duelgen
import unittest


class TestDay15(unittest.TestCase):
    def test_judge(self):
        result = duelgen()
        expected = 619
        self.assertEqual(result, expected)

    # def test_judge_2(self):
    #     genA = 591
    #     genB = 393
    #     result = judge(genA, genB, multipliesA=4, multipliesB=8, N=5*10**6)
    #     expected = 290
    #     self.assertEqual(result, expected)
