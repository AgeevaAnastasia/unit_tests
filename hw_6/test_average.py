import pytest
from average import ListsOfNums


@pytest.fixture
def lst1():
    return [2, 5, 3, 6]


@pytest.fixture
def lst2():
    return [3, 5, 1]


# Проверка правильности вычислений средних значений непустых списков
def test_get_averages(lst1, lst2):
    two_lists = ListsOfNums(lst1, lst2)
    assert two_lists.get_averages() == (
        4,
        3,
    ), "Тест на вычисление средних значений двух непустых списков провален"


# Проверка средних значений одно и/или обоих пустых списков
@pytest.mark.parametrize(
    "lst1, lst2, result",
    [([2, 5, 3, 6], [], (4, 0)), ([], [3, 5, 1], (0, 3)), ([], [], (0, 0))],
)
def test_get_averages_of_empty_list(lst1, lst2, result):
    two_lists = ListsOfNums(lst1, lst2)
    assert (
        two_lists.get_averages() == result
    ), "Тест на вычисление средних значений одного и/или обоих пустых списков провален"


def test_avg1_eq_avg2(lst1):
    lst2 = lst1
    two_lists = ListsOfNums(lst1, lst2)
    assert (
        two_lists.compare_averages() == "Средние значения равны"
    ), "Тест на равенство средних значений провален"


def test_avg1_gt_avg2(lst1, lst2):
    two_lists = ListsOfNums(lst1, lst2)
    assert (
        two_lists.compare_averages() == "Первый список имеет большее среднее значение"
    ), "Тест на большее среднее значение первого списка провален"


def test_avg2_gt_avg1(lst1, lst2):
    two_lists = ListsOfNums(lst2, lst1)
    assert (
        two_lists.compare_averages() == "Второй список имеет большее среднее значение"
    ), "Тест на большее среднее значение второго списка провален"
