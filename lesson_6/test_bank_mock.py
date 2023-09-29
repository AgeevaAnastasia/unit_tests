# test


import pytest
from unittest.mock import Mock

from task_4_bank_mock import Bank, Person


@pytest.fixture
def setup():
    bank = Mock()
    person = Person()
    person.add_money(100)
    return bank, person


def test_receive_money(setup):
    bank, person = setup
    person.transfer_money(bank, 100)
    bank.receive_money.assert_called_with(100)
    print(bank.__dict__)


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
