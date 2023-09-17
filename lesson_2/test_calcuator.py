import unittest

from task_1_calculator import calculator


class TestCalculator(unittest.TestCase):
    def test_div_on_zero(self):
        self.assertRaises(ArithmeticError, calculator.calculate, 1, 0, '/')

    def test_wrong_operator(self):
        self.assertRaises(ValueError, calculator.calculate, 1, 1, 'a')

    def test_pow_positive_numbers(self):
        self.assertEqual(calculator.pow(2.0, 3.0), 8.0)

    def test_pow_zero_exponent(self):
        self.assertEqual(calculator.pow(2.0, 0.0), 1.0)

    def test_pow_one_exponent(self):
        self.assertEqual(calculator.pow(2.0, 1.0), 2.0)

    def test_pow_negative_base(self):
        self.assertEqual(calculator.pow(-2.0, 3.0), -8.0)

    def test_pow_negative_exponent(self):
        self.assertEqual(calculator.pow(2.0, -1.0), 0.5)
