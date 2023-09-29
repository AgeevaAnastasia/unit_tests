# Задание №4
# В предыдущем задании используйте unittest.mock для создания мок-объекта Bank.
# Напишите тест, в котором вы проверите, вызывается ли метод receive_money с правильным аргументом.


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


