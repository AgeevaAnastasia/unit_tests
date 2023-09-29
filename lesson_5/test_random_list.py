import unittest

from task_1_random_list import get_random_list
from task_1_max_num import get_max_num


class TestRnd(unittest.TestCase):
    def test_rnd(self):
        lst = get_random_list(10)
        self.assertEqual(get_max_num(lst), sorted(lst)[-1])
