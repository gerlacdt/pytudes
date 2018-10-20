from day14 import defrag, region
import unittest


class TestDay14(unittest.TestCase):
    def test_defrag(self):
        input1 = "oundnydw"
        result = defrag(input1)
        expected = 8106
        self.assertEqual(result, expected)

    def test_region(self):
        # input1 = "flqrgnkx"
        input1 = "oundnydw"
        result = region(input1)
        expected = 1164
        self.assertEqual(result, expected)
