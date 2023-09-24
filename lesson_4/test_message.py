import unittest
from unittest.mock import patch

from task_5_message import NotificationService


class TestBook(unittest.TestCase):
    # @patch перехватывает все обращения и заменяет их на mock-объект
    @patch('task_5_message.MessageService')
    def test_message(self, mock_message):
        self.notification_service = NotificationService(mock_message)
        message = 'Hello'
        recipient = 'user'
        self.notification_service.message_service(message, recipient)
        self.notification_service.message_service.assert_called_once_with(message, recipient)
