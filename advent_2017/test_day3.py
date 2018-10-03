import day3
import unittest


class TestDay3(unittest.TestCase):
    def test_spiral(self):
        result = day3.spiral(277678)
        expected = 475
        self.assertEqual(result, expected)
