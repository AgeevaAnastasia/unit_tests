import unittest

from task_6_user import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('login', 'password')

    def test_successful_authenticate(self):
        self.user.authenticate(self.user.login, self.user.password)
        self.assertTrue(self.user.is_authenticate)

    def test_failed_authenticate_wrong_login(self):
        self.user.authenticate('', self.user.password)
        self.assertFalse(self.user.is_authenticate)

    def test_failed_authenticate_wrong_password(self):
        self.user.authenticate(self.user.login, '')
        self.assertFalse(self.user.is_authenticate)

    def test_failed_authenticate_wrong_login_and_password(self):
        self.user.authenticate('', '')
        self.assertFalse(self.user.authenticate('', ''))
