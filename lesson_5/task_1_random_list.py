from random import randint


def get_random_list(size: int) -> list[int]:
    return [randint(0, 100) for _ in range(size)]
