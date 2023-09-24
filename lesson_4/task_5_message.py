# Задание №5
# Вам нужно написать тест с использованием моков для сервиса отправки сообщений.
# Условие: У вас есть класс MessageService с методом public void sendMessage(String message, String
# recipient), который отправляет сообщение получателю.
# Вам необходимо проверить правильность работы класса NotificationService, который использует
# MessageService для отправки уведомлений.
from random import choice


class MessageService:
    def send_message(self, message: str, recipient: str) -> str:
        result = choice(['', 'не '])
        return f'Сообщение "{message}" для получателя {recipient} {result}отправлено.'


class NotificationService:
    def __init__(self, message_service: MessageService):
        self._message_service = message_service

    @property
    def message_service(self):
        return self._message_service

    def send_notification(self, message: str, recipient: str) -> str:
        return self._message_service.send_message(message, recipient)


if __name__ == '__main__':
    message_service = MessageService()
    notification_service = NotificationService(message_service)
    print(notification_service.send_notification('Hello', 'user'))