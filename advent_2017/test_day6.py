import unittest
import day6
from myutils import readFile


class TestDay6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        filename = 'data/input6.txt'
        cls.content = readFile(filename)

    def test_read_banks(self):
        banks = day6.readBanks(self.content)
        expected = 16
        self.assertEqual(len(banks), expected)

    def test_mem_alloc(self):
        input = '0 2 7 0'
        banks = day6.readBanks(input)

        result = day6.mem_realloc(banks)
        expected = (5, 4)
        self.assertEqual(result, expected)

    def test_mem_alloc_file(self):
        banks = day6.readBanks(self.content)

        result = day6.mem_realloc(banks)
        expected = (7864, 1695)
        self.assertEqual(result, expected)
