import unittest

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = multiply(4, 2)
        self.assertEqual(result, 8)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0) 
