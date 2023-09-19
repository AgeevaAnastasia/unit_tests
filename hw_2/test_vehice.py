"""Проект Vehicle. Написать следующие тесты с использованием unittest:

- Проверить, что экземпляр объекта Car также является экземпляром
транспортного средства (используя оператор isinstance).

- Проверить, что объект Car создается с 4-мя колесами.

- Проверить, что объект Motorcycle создается с 2-мя колесами.

- Проверить, что объект Car развивает скорость 60 в режиме тестового вождения
(используя метод testDrive()).

- Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения
(используя метод testDrive()).

- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция
движения транспорта) машина останавливается (speed = 0).

- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция
движения транспорта) мотоцикл останавливается (speed = 0)."""

import unittest
from class_vehicle import Vehicle, Car, Motorcycle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Lada', 'XRAY', 2022)
        self.motorcycle = Motorcycle('Jawa', '660 Sportard', 2022)

    # Экземпляр объекта Car также является экземпляром транспортного средства:
    def test_car_is_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle), 'Тест на принадлежность к абстрактному классу Vehicle не прошёл')

    # объект Car создается с 4-мя колесами:
    def test_car_4_wheels(self):
        self.assertEqual(self.car.num_wheels, 4, 'Тест на количество колес автомобиля = 4 не прошёл')

    # объект Motorcycle создается с 2-мя колесами:
    def test_motorcycle_2_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2, 'Тест на количество колес мотоцикла = 2 не прошёл')

    # объект Car развивает скорость 60 в режиме тестового вождения:
    def test_car_testdrive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60, 'Тест на скорость автомобиля на тестдрайве = 60 не прошёл')

    # объект Motorcycle развивает скорость 75 в режиме тестового вождения:
    def test_motorcycle_testdrive(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75, 'Тест на скорость мотоцикла на тестдрайве = 75 не прошёл')

    # в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
    # машина останавливается (speed = 0):
    def test_car_park(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0, 'Тест на остановку автомобиля не прошёл')

    # в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
    # мотоцикл останавливается (speed = 0):
    def test_motorcycle_park(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0, 'Тест на остановку мотоцикла не прошёл')
