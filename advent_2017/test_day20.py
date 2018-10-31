from day20 import swarm, INPUT1
import unittest


class TestDay20(unittest.TestCase):
    def test_swarm(self):
        result = swarm(INPUT1)
        expected = 0
        self.assertEqual(result, expected)
