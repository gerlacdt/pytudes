import day5
import unittest
from myutils import readFile


class TestDay4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        filename = 'data/input5.txt'
        cls.content = readFile(filename)

    def test_maze(self):
        content = '''0
3
0
1
-3
'''
        result = day5.maze(day5.readInstructions(content))
        result2 = day5.maze2(day5.readInstructions(content))
        expected = 5
        expected2 = 10
        self.assertEqual(result, expected)
        self.assertEqual(result2, expected2)


    def test_maze_input(self):
        result = day5.maze(day5.readInstructions(self.content))
        expected = 356945
        self.assertEqual(result, expected)

        result2 = day5.maze2(day5.readInstructions(self.content))
        expected2 = 28372145
        self.assertEqual(result2, expected2)
