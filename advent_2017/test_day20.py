from day20 import swarm, collision, INPUT1
import unittest


class TestDay20(unittest.TestCase):
    def test_swarm(self):
        result = swarm(INPUT1, 500)
        expected = 150
        self.assertEqual(result, expected)

    def test_collision(self):
        result = collision(INPUT1, 100)
        expected = 657
        self.assertEqual(result, expected)
