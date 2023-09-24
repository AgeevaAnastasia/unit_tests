# Задание №7
# Вам нужно написать тест с использованием моков для класса, который выполняет HTTP-запросы.
# Условие: У вас есть класс HttpClient с методом public String get(String url), который выполняет
# HTTP-запрос и возвращает результат. Вам необходимо проверить правильность работы класса
# WebService, который использует HttpClient для получения данных с веб-сайта.
from random import randint


class HttpClient:
    def get(self, url: str) -> str:
        return f'Server response is {randint(100, 599)}'

    def put(self, url: str) -> str:
        return f'Server response is {randint(100, 599)}'


class WebService:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def make_request(self, url: str, request: str):
        response = self.http_client.get(url)
        return f'На запрос "{request}" пришёл ответ {response}'


if __name__ == '__main__':
    httpclient = HttpClient()
    webservice = WebService(httpclient)
    print(webservice.make_request('https://google.com', 'weather'))
