"""Предположим, у вас есть класс WeatherService, который имеет метод getCurrentTemperature(),
обращающийся к внешнему API для получения информации о текущей температуре.
Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService.
Создайте мок-объект для WeatherService с использованием Mockito.
"""
import random


class WeatherService:
    def get_current_temperature(self) -> int: # в случае реального сервиса здесь был бы http запрос ко внешнему ресурсу. Но здесь просто демонстрация
        return random.randint(0, 30)


class WeatherReporter:
    def __init__(self, weather_service: WeatherService):
        self._weather_service = weather_service

    @property
    def weather_service(self):
        return self._weather_service

    def generate_report(self):
        self._weather_service.get_current_temperature()
