import day1
import unittest


class TestDay1(unittest.TestCase):
    def test_captcha_no_match(self):
        l = [1, 2, 3]
        result = day1.captcha(l)
        expected = 0
        self.assertEqual(result, expected)

    def test_captcha(self):
        d = {'1122': {'data': [1, 1, 2, 2], 'expected': 3},
             '1111': {'data': [1, 1, 1, 1], 'expected': 4},
             '1234': {'data': [1, 2, 3, 4], 'expected': 0},
             '91212129': {'data': [9, 1, 2, 1, 2, 1, 2, 9], 'expected': 9},
             '412344': {'data': [4, 1, 2, 3, 4, 4], 'expected': 8},
             '11211': {'data': [1, 1, 2, 1, 1], 'expected': 3}
        }

        for name, case in d.items():
            result = day1.captcha(case['data'])
            self.assertEqual(result, case['expected'],
                             "TestCase name: %s".format(name))
