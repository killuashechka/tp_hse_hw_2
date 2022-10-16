import unittest
import func

class Test(unittest.TestCase):
  def test_new(self):
        mas_test = [-2,7,5,2,-5]
        if func.Arithmetic._mult(mas_test) == math.factorial(max(mas_test)):
            prin = "Факториал максимального числа равен произведению всех чисел"
        else:
            prin = "Факториал максимального числа не равен произведению всех чисел"
        self.assertEqual(prin, "Факториал максимального числа не равен произведению всех чисел")
unittest.main()