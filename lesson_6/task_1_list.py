# Задание №1
# Напишите функцию для поиска среднего значения в списке чисел и соответствующие юнит-тесты
# с использованием фреймворка pytest.

def find_average(lst: list[int | float]) -> float:
    for item in lst:
        if not isinstance(item, (int, float)):
            raise ValueError(f'Element {item} not int or float')
    if len(lst):
        return sum(lst) / len(lst)
    return 0.0


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 'a']
    print(find_average(lst))
