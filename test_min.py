import unittest
import func


class Test(unittest.TestCase):
  time = 1
  def test_min(self):
          self.assertEqual(func.Arithmetic._min([-2,7,5,2,-5] * self.time), -5)
unittest.main()