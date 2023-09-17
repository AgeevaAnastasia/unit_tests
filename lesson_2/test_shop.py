import io
import unittest
from unittest.mock import patch

from task_2_shop import Shop, Product, Cart


class TestShop(unittest.TestCase):
    def setUp(self) -> None:
        product_names = ("bacon", "beef", "ham", "salmon", "carrot", "potato",
                         "onion", "apple", "melon", "rice", "eggs", "yogurt")
        product_prices = (170.00, 250.00, 200.00, 150.00, 15.00, 30.00, 20.00,
                          59.00, 88.00, 100.00, 80.00, 55.00)
        stock = (10, 3, 10, 10, 10, 10, 10, 70, 13, 30, 40, 60)

        self.products = []
        for product_args in zip(product_prices, product_names, range(1, len(stock) + 1), stock):
            self.products.append(Product(*product_args))

        self.shop = Shop(self.products)
        self.cart = Cart(self.shop)

    # 2.1. Разработайте модульный тест для проверки, что общая стоимость
    # корзины с разными товарами корректно рассчитывается
    def test_price_cart_is_correct_calculated(self):
        self.cart.add_product_by_id(1)
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(1)
        self.assertEqual(self.cart.total_price, 790)

    # 2.2. Создайте модульный тест для проверки, что общая стоимость
    # корзины с множественными экземплярами одного и того же продукта корректно рассчитывается.
    def test_price_cart_products_same_type_is_correct_calculated(self):
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.cart.add_product_by_id(7)
        self.assertEqual(self.cart.total_price, 700)

    # 2.3. Напишите модульный тест для проверки, что при удалении
    # товара из корзины происходит перерасчет общей стоимости корзины.
    def test_recalculation_after_remove_product_from_cart(self):
        self.cart.add_product_by_id(3)
        self.cart.add_product_by_id(10)
        self.cart.remove_product_by_id(3)
        self.assertEqual(self.cart.total_price, 100)

    # 2.4. Разработайте модульный тест для проверки, что при добавлении определенного количества товара в корзину,
    # общее количество этого товара в магазине соответствующим образом уменьшается.
    def test_changing_quantity_products_store(self):
        self.cart.add_product_by_id(1)
        self.assertEqual(self.shop.get_product_by_id(1).quantity, 9)

    # 2.5. Создайте модульный тест для проверки, что если пользователь забирает все имеющиеся продукты
    # определенного типа из магазина, эти продукты больше не доступны для заказа.
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buying_last_store_product(self, mock_stdout):
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(2)
        self.cart.add_product_by_id(2)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Этого товара нет в наличии')


    # 2.6. Напишите модульный тест для проверки, что при удалении товара из корзины,
    # общее количество этого товара в магазине соответствующим образом увеличивается.
    def test_return_product_in_shop_after_remove_from_cart(self):
        self.cart.add_product_by_id(1)
        self.cart.add_product_by_id(1)
        self.cart.remove_product_by_id(1)
        self.assertEqual(self.shop.get_product_by_id(1).quantity, 9)

    # 2.7. Разработайте параметризованный модульный тест для проверки,
    # что при вводе неверного идентификатора товара генерируется исключение RuntimeError.
    def test_select_incorrect_product_id_exception(self):
        self.assertRaisesRegex(RuntimeError, 'Не найден продукт с ID: 20',
                               self.cart.add_product_by_id, id_=20)

    # 2.8. Создайте модульный тест для проверки, что при попытке удалить из корзины больше товаров,
    # чем там есть, генерируется исключение RuntimeError.
    def test_remove_products_from_cart_more_then_exist_exception(self):
        self.assertRaisesRegex(RuntimeError, 'В корзине не найден товар с ID: 1',
                               self.cart.remove_product_by_id, id_=1)

