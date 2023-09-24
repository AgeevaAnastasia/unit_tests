"""Разработайте и протестируйте метод numberInInterval, который проверяет,
попадает ли переданное число в интервал (25;100)"""
import unittest


def num_interval(n: int) -> bool:
    return n in range(25, 100)


class TestNumInInterval(unittest.TestCase):

    def test_in_interval(self):
        self.assertTrue(num_interval(26), 'Тест на нахождение числа в интервале провален')

    def test_out_interval(self):
        self.assertFalse(num_interval(101), 'Тест на нахождение числа в интервале провален')
