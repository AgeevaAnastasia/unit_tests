"""Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет,
является ли переданное число четным или нечетным"""
import unittest


def even_odd_num(n: int) -> bool:
    return n % 2 == 0


class TestEvenOddNum(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even_odd_num(2), 'Тест на четное/нечетное провален')

    def test_odd(self):
        self.assertFalse(even_odd_num(1), 'Тест на четное/нечетное провален')

