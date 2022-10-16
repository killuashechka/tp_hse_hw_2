import unittest
import func
import math

class Test(unittest.TestCase):
    time = 1
    def test_sum(self):
        self.assertEqual(func.Arithmetic._sum([-2,7,5,2,-5] * self.time), 7 * self.time)
    def test_max(self):
        self.assertEqual(func.Arithmetic._max([-2,7,5,2,-5] * self.time), 7)
    def test_min(self):
        self.assertEqual(func.Arithmetic._min([-2,7,5,2,-5] * self.time), -5)
    def test_mult(self):
        self.assertEqual(func.Arithmetic._mult([-2,7,5,2,-5] * self.time), 700 ** self.time)
    def test_new(self):
        mas_test = [-2,7,5,2,-5]
        if func.Arithmetic._mult(mas_test) == math.factorial(max(mas_test)):
            print("Факториал максимального числа равен произведению всех чисел")
        else:
            print("Факториал максимального числа не равен произведению всех чисел")

unittest.main()