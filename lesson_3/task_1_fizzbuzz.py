

def fizz_buzz(num: int) -> str:
    assert type(num) == int, 'Вы передали параметр не типа int'
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    return str(num)
