import itertools
import unittest
import countdown

class TestCountDown(unittest.TestCase):
 def test_countdown2016(self):
  result = countdown.countdown(2016)
  expected = "((((((((10*9)*(8+7))-6)+5)-4)*3)/2)-1)"
  self.assertEqual(result, expected)

 def test_iter_product(self):
  x = itertools.product({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'})
  for a in x:
   print a


if __name__ == '__main__':
    unittest.main()
