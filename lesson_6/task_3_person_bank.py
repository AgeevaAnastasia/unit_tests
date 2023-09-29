# Задание №3
# Создайте два класса: Person и Bank. Класс Person должен иметь метод transfer_money,
# который позволяет перевести деньги в Bank. Класс Bank должен иметь метод
# receive_money.
# Напишите тесты, проверяющие корректность взаимодействия этих классов.

class Bank:
    def __init__(self):
        self.repo = 0.0

    def receive_money(self, money: float) -> None:
        self.repo += money


class Person:
    def __init__(self):
        self.balance = 0.0

    def add_money(self, money: float) -> None:
        self.balance += money

    def transfer_money(self, bank: Bank, money):
        if self.balance >= money > 0:
            bank.receive_money(money)
            self.balance -= money
        else:
            raise ValueError('Problem with your money or balance')