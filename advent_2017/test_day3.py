import day3
import unittest


class TestDay3(unittest.TestCase):
    def test_spiral(self):
        result = day3.spiral(325489)
        expected = 552
        self.assertEqual(result, expected)

    def test_spiral2(self):
        result = day3.spiral2(325489)
        expected = 330785
        self.assertEqual(result, expected)
