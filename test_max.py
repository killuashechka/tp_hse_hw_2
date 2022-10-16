import unittest
import func

class Test(unittest.TestCase):
  time = 1
  def test_max(self):
        self.assertEqual(func.Arithmetic._max([-2,7,5,2,-5] * self.time), 7)
unittest.main()