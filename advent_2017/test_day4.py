import day4
import unittest


class TestDay4(unittest.TestCase):
    def test_passphrase(self):
        filename = 'data/input4.txt'
        content = day4.readFile(filename)
        result = day4.isValid(content)
        expected = 383
        self.assertEqual(result, expected)
