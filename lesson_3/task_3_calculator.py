def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if purchase_amount < 0:
        raise ValueError('Сумма не может быть меньше 0')

    if not 0 <= discount_amount <= 100:
        raise ValueError('Скидка должна быть в промежутке от 0 до 100')

    return purchase_amount - purchase_amount * discount_amount / 100
