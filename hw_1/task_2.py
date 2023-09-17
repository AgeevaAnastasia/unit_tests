"""Мы хотим улучшить функциональность нашего интернет-магазина.
Ваша задача - добавить два новых метода в класс Shop:
Метод sortProductsByPrice(), который сортирует список продуктов по стоимости.
Метод getMostExpensiveProduct(), который возвращает самый дорогой продукт.
Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов
(правильное количество продуктов, верное содержимое корзины).
Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
Напишите тесты для проверки корректности работы метода sortProductsByPrice
(проверьте правильность сортировки).
Используйте класс Product для создания экземпляров продуктов и класс Shop для
написания методов сортировки и тестов."""

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} {self.price}'


class Shop:

    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def get_shop(self):
        shop_products = ''
        for product in self.product_list:
            shop_products += str(product.name) + ' ' + str(product.price) + '\n'
        return shop_products

    def sort_products_by_price(self):
        self.product_list.sort(key=lambda product: product.price)

    def get_most_expensive_product(self):
        copy_product_list = self.product_list.copy()
        copy_product_list.sort(key=lambda product: product.price, reverse=True)
        return copy_product_list[0]

    # Тест, чтобы проверить, что магазин хранит верный список продуктов (правильное количество продуктов, верное содержимое корзины).
    def test_len_and_contain_shop(self):
        self.product_list.clear()
        test_list = []
        product_1 = Product('Milk', 100)
        test_list.append(product_1)
        product_2 = Product('Bread', 50)
        test_list.append(product_2)
        product_3 = Product('Butter', 150)
        test_list.append(product_3)
        self.add_product(product_1)
        self.add_product(product_2)
        self.add_product(product_3)
        assert len(self.product_list) == 3, 'test_len_shop failed'
        print('test_len_shop is OK')
        assert test_list == self.product_list, 'test_contain_shop failed'
        print('test_contain_shop is OK')

    # Тест для проверки корректности работы метода getMostExpensiveProduct.
    def test_get_most_expensive_product(self):
        # поиск самого дорогого продукта альтернативным способом
        most_expensive_product = self.product_list[0]
        for i in range(1, len(self.product_list)):
            if self.product_list[i].price > most_expensive_product.price:
                most_expensive_product = self.product_list[i]
        assert most_expensive_product == self.get_most_expensive_product(), 'test_get_most_expensive_product failed'
        print('test_get_most_expensive_product is OK')

    # Тест для проверки корректности работы метода sortProductsByPrice (правильность сортировки).
    def test_sort_products_by_price(self):
        # тестовый список продуктов, отсортированный другой функцией
        test_list = sorted(self.product_list, key=lambda product: product.price)
        self.sort_products_by_price()
        # поиндексное сравнение отсортированных списков
        assert test_list == self.product_list, 'test_sort_products_by_price failed'
        print('test_sort_products_by_price is OK')


if __name__ == '__main__':
    shop = Shop()
    shop.add_product(Product('Milk', 100))
    shop.add_product(Product('Bread', 50))
    shop.add_product(Product('Butter', 150))
    print(f'Shop list: \n{shop.get_shop()}')
    shop.sort_products_by_price()
    print(f'Shop list after sorting by price: \n{shop.get_shop()}')
    print(f'Самый дорогой продукт: {shop.get_most_expensive_product()}')

    shop.test_sort_products_by_price()
    shop.test_get_most_expensive_product()
    shop.test_len_and_contain_shop()