"""В этом проекте, вы будете работать с проектом ""Vehicle"",
который представляет собой иерархию классов, включающую абстрактный
базовый класс ""Vehicle"" и два его подкласса ""Car"" и ""Motorcycle"".

Базовый класс ""Vehicle"" содержит абстрактные методы ""testDrive()"" и ""park()"",
а также поля ""company"", ""model"", ""yearRelease"", ""numWheels"" и ""speed"".

Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы.
При создании объекта ""Car"", число колес устанавливается в 4, а скорость в 0.
В методе ""testDrive()"" скорость устанавливается на 60, а в методе ""park()"" - обратно в 0.

Класс ""Motorcycle"" также расширяет ""Vehicle"" и реализует его абстрактные методы.
При создании объекта ""Motorcycle"", число колес устанавливается в 2, а скорость в 0.
В методе ""testDrive()"" скорость устанавливается на 75, а в методе ""park()"" - обратно в 0."""


from abc import ABC, abstractmethod


class Vehicle(ABC):
    company = ''
    model = ''
    year_release = 0
    num_wheels = 0
    speed = 0

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass


class Car(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def __str__(self):
        return f'Company: {self.company}, Model: {self.model}, ' \
               f'\nYear: {self.year_release}, Speed: {self.speed}\n'


class Motorcycle(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def __str__(self):
        return f'Company: {self.company}, Model: {self.model}, ' \
               f'\nYear: {self.year_release}, Speed: {self.speed}\n'


if __name__ == '__main__':
    car = Car('Lada', 'XRAY', 2022)
    car.test_drive()
    print(car)
    car.park()
    print(car)

    motorcycle = Motorcycle('Jawa',  '660 Sportard', 2022)
    motorcycle.test_drive()
    print(motorcycle)
    motorcycle.park()
    print(motorcycle)
