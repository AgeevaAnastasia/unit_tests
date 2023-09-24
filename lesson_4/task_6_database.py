# Задание №6
# Вам требуется протестировать класс, который обрабатывает запросы к базе данных.
# Условие: У вас есть класс Database с методом public List<String> query(String sql), который выполняет SQL-
# запрос и возвращает результат.
# Вам необходимо проверить правильность работы класса DataProcessor, который использует Database для
# выполнения запроса и обработки результатов.
from random import randint, sample
from string import ascii_lowercase


class Database:
    def query(self, sql: str) -> list:
        result = []
        for _ in range(randint(0, 10)):
            word = ''.join(sample(ascii_lowercase, 5)).capitalize()
            result.append(word)
        return result


class DataProcessor:
    def __init__(self, database: Database):
        self._database = database

    @property
    def database(self):
        return self._database

    def db_query(self, sql: str) -> str:
        result = self._database.query(sql)
        # print(result)
        # result = ' '.join(result)
        return f'Результат вашего запроса "{sql}": {result}'


if __name__ == '__main__':
    database = Database()
    data_processor = DataProcessor(database)
    print(data_processor.db_query('select * from abstract_table'))
