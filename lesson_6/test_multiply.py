# test

import pytest

from task_6_multiply import multiply


# запуск тестов с разными параметрами
@pytest.mark.parametrize('a, b, result', [
    (10, 0, 0),
    (10, 1, 10),
    (10, 10, 100),
    (-100, 10, -1000)
])
def test_param(a, b, result):
    assert multiply(a, b) == result, 'test_param failed'


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
