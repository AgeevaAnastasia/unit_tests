# Задание №2
# Модифицируйте функцию find_average так, чтобы она вызывала исключение TypeError,
# если ей передается не список.
# Напишите тест, который проверяет вызов этого исключения

def find_average(lst: list[int | float]) -> float:
    if not isinstance(lst, list):
        raise TypeError('Argument must be a list type')
    return sum(lst) / len(lst)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    lst = 1
    print(find_average(lst))
