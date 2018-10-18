import day13
import unittest
from myutils import readFile


class TestDay13(unittest.TestCase):
    def test_scanner(self):
        content = readFile('./data/input13.txt')
        scanners = day13.read(content)
        result = day13.trip_severity(scanners)
        expected = 632
        self.assertEqual(result, expected)

    def test_safe_pass(self):
        content = readFile('./data/input13.txt')
        scanners = day13.read(content)
        result = day13.safe_delay(scanners)
        expected = 3849742
        self.assertEqual(result, expected)
