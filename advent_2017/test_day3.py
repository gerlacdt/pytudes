import day3
import utils
import unittest


class TestDay3(unittest.TestCase):
    s = '''17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23
'''

    def test_findCenter(self):
        rows = utils.Array(self.s)
        x, y = day3.findCenter(rows)
        ex, ey = 2, 2
        self.assertEqual(x, ex)
        self.assertEqual(y, ey)

    def test_findCenter_fail(self):
        s = '''2 3 4
5 6 7
'''
        with self.assertRaises(RuntimeError):
            rows = utils.Array(s)
            x, y = day3.findCenter(rows)

    def test_dist(self):
        rows = utils.Array(self.s)
        x, y = day3.findCenter(rows)

        # test cases, (dest-x,dest-y, distance)
        tests = ((2, 2, 0), (4, 1, 3), (2, 4, 2))

        for t in tests:
            result = day3.calcManhattanDistance((x, y), (t[0], t[1]))
            expected = t[2]
            self.assertEqual(result, expected)

    def test_spiral(self):
        result = day3.spiral(self.s)
        expected = 53
        self.assertEqual(result, expected)
