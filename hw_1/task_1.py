"""В классе Calculator создайте метод calculateDiscount, который принимает
сумму покупки и процент скидки и возвращает сумму с учетом скидки.
Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
Если метод calculateDiscount получает недопустимые аргументы, он должен
выбрасывать исключение ArithmeticException.
Не забудьте написать тесты для проверки этого поведения."""


class Calculator:

    def calculate_discount(self, amount: float, discount: int) -> float:
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise ArithmeticError(f'Недопустимое значение параметра {amount = }')
        if not (isinstance(discount, int) and (discount in range(0, 101))):
            raise ArithmeticError(f'Недопустимое значение параметра {discount = }')
        result = amount * (100 - discount) / 100
        return result


def test_invalid_amount_arg(calculator: Calculator):
    try:
        calculator.calculate_discount('oups', 10)
        raise Exception('Ожидалась ошибка "ArithmeticError", но получился неожиданный результат')
    except Exception as e:
        print(f'Тест на неверный аргумент параметра суммы пройден. Как и ожидалось, возникла ошибка "{e}"')


def test_invalid_discount_arg(calculator: Calculator):
    try:
        calculator.calculate_discount(500, '10')
        raise Exception('Ожидалась ошибка "ArithmeticError", но получился неожиданный результат')
    except Exception as e:
        print(f'Тест на неверный аргумент параметра скидки пройден. Как и ожидалось, возникла ошибка "{e}"')


def test_invalid_discount_num(calculator: Calculator):
    for i in range(0, 101):
        assert calculator.calculate_discount(100, i) == 100 * (100 - i) / 100, \
            f'Тест на значения параметра discount не пройден, возникла ошибка на проценте "{i}"'
    print('Тест на значения скидки от 0 до 100% пройден')


if __name__ == '__main__':
    calculator = Calculator()
    test_invalid_amount_arg(calculator)
    test_invalid_discount_arg(calculator)
    test_invalid_discount_num(calculator)
