# pytest

import pytest

from task_2_list_avg import find_average


def test_find_average_raise():
    lst = 3
    with pytest.raises(TypeError):
        find_average(lst)


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
