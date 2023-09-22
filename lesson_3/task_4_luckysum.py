def lucky_sum(a: int, b: int, c: int) -> int:
    if a == b == c == 13:
        raise ValueError('Все числа равны 13')

    return sum(filter(lambda x: x != 13, (a, b, c)))