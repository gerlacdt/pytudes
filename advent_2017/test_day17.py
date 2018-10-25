import day17
import unittest


class TestDay17(unittest.TestCase):
    def test_spinlock(self):
        result = day17.spinlock(324)
        expected = 1306
        self.assertEqual(result, expected)

    def test_angry_spinlock(self):
        result = day17.angry_spinlock(324, N=50*10**6)
        expected = 20430489
        self.assertEqual(result, expected)
