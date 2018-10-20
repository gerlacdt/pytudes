from day14 import defrag
import unittest


class TestDay14(unittest.TestCase):
    def test_defrag(self):
        input1 = "oundnydw"
        result = defrag(input1)
        expected = 8106
        self.assertEqual(result, expected)
