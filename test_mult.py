import unittest
import func


class Test(unittest.TestCase):
    time = 1
    def test_mult(self):
        self.assertEqual(func.Arithmetic._mult([-2,7,5,2,-5] * self.time), 700 ** self.time)
    
unittest.main()