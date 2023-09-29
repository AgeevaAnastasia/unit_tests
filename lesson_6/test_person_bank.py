# pytest

import pytest

from task_3_person_bank import Bank, Person


@pytest.fixture
def setup():
    bank = Bank()
    person = Person()
    person.add_money(100)
    return bank, person


def test_transfer_money(setup):
    bank, person = setup
    start_balance = bank.repo
    person.transfer_money(bank, 50)
    assert person.balance == 50, 'test_transfer_money failed'
    assert start_balance + 50 == 50, 'test_transfer_money failed'


def test_transfer_higher_money(setup):
    bank, person = setup
    start_balance = bank.repo
    person.transfer_money(bank, 150)
    assert person.balance == 100, 'test_transfer_higher_money'
    assert start_balance == 0, 'test_transfer_higher_money'


def test_transfer_negative_money(setup):
    bank, person = setup
    with pytest.raises(ValueError):
        person.transfer_money(bank, -1)


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
