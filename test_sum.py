import unittest
import func

class Test(unittest.TestCase):
    time = 1
    def test_sum(self):
        self.assertEqual(func.Arithmetic._sum([-2,7,5,2,-5] * self.time), 7 * self.time)
unittest.main()