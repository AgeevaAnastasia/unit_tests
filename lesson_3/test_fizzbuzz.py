import unittest

from task_1_fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_15(self):
        self.assertEqual(fizz_buzz(45), 'fizzbuzz')

    def test_fizzbuzz_3(self):
        self.assertEqual(fizz_buzz(9), 'fizz')

    def test_fizzbuzz_5(self):
        self.assertEqual(fizz_buzz(10), 'buzz')

    def test_fizzbuzz_nothing(self):
        self.assertEqual(fizz_buzz(11), '11')
