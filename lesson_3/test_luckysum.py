import unittest

from task_4_luckysum import lucky_sum


class TestLuckysum(unittest.TestCase):
    def test_all_num_13_exception(self):
        self.assertRaisesRegex(ValueError, 'Все числа равны 13',
                               lucky_sum, a=13, b=13, c=13)

    def test_one_num_is_13(self):
        self.assertEqual(lucky_sum(4, 5, 13), 9)
        self.assertEqual(lucky_sum(4, 13, 5), 9)
        self.assertEqual(lucky_sum(13, 4, 5), 9)

    def test_two_nums_are_13(self):
        self.assertEqual(lucky_sum(13, 13, 5), 5)
        self.assertEqual(lucky_sum(13, 5, 13), 5)
        self.assertEqual(lucky_sum(5, 13, 13), 5)

    def test_lucky_sum(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)

