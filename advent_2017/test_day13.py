import day13
import unittest
from myutils import readFile


class TestDay13(unittest.TestCase):
    def test_scanner(self):
        content = readFile('./data/input13.txt')
        result = day13.scanner(content)
        expected = 632

        self.assertEqual(result, expected)
