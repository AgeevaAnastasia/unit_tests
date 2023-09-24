import unittest
from unittest.mock import Mock

from task_2_payment import PaymentForm


class TestPayment(unittest.TestCase):
    def setUp(self) -> None:
        self.payment_form = PaymentForm(Mock())

    def test_pay_calls_charge(self):
        self.payment_form.pay(54.9)
        self.payment_form.credit_card.charge.assert_called_once()
