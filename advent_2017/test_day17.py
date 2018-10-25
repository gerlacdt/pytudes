import day17
import unittest


class TestDay17(unittest.TestCase):
    def test_spinlock(self):
        result = day17.spinlock(324)
        expected = 1306
        self.assertEqual(result, expected)
