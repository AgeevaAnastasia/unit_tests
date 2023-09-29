import unittest

from task_2_user_service import UserService
from task_2_user_repository import UserRepository


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user_service = UserService(UserRepository())

    def test_user(self):
        self.assertEqual(self.user_service.get_user_name(3), 'User 3')
