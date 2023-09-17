import sys

from task_2_shop import Shop, Cart, Product


class UserInterface:
    def __init__(self, shop: Shop):
        self.shop = shop
        self.cart = Cart(self.shop)

    def _start_screen(self):
        print('Выберите одно из действий:\n1. Перейти к выбору продуктов\n'
              '2. Показать продукты в корзине\n0. Выход\nВвод: ', end='')

    def _store_products_menu(self):
        print('Выберите одно из действий:\n1. Добавить в корзину\n'
              '2. Удалить из корзины\n0. Выход\nВвод: ', end='')

    def _display_store_products(self):
        form = '{:>3}|{:<20}|{:<9}|{:<3}'
        print('Доступные продукты в магазине:')
        print(form.format("ID", "Название", "Цена, р.", "Кол-во в корзине, шт."))
        for product in self.shop.products:
            print(form.format(product.id, product.title, product.cost, product.quantity))
        print()

    def _inner_choice(self):
        self._store_products_menu()
        user_choice = int(input())
        match user_choice:
            case 1:
                id_ = int(input("Введите ID продукта, который хотите добавить в корзину: "))
                self.cart.add_product_by_id(id_)
            case 2:
                id_ = int(input("Введите ID продукта, который хотите удалить: "))
                self.cart.remove_product_by_id(id_)

    def menu(self):
        while True:
            self._start_screen()
            user_choice = int(input())
            match user_choice:
                case 1:
                    self._display_store_products()
                    self._inner_choice()
                case 2:
                    self.cart.print_cart_items()
                case 0:
                    sys.exit()


if __name__ == '__main__':
    product = Product(80, 'Milk', 1, 20)
    shop = Shop(products=[product])
    user_interface = UserInterface(shop)
    user_interface.menu()
