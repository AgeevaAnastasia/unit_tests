class Product:
    def __init__(self, cost: int, title: str, id_: int, quantity: int):
        self._cost = cost
        self._title = title
        self._id = id_
        self.quantity = quantity

    @property
    def cost(self):
        return self._cost

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash((self.cost, self.title))

    def __repr__(self):
        return f"Product({self.cost}, '{self.title}', {self.id}, {self.quantity})"


class Shop:
    def __init__(self, products: list[Product]):
        self._products = products

    @property
    def products(self):
        return self._products

    def get_product_by_id(self, id_: int) -> Product:
        for product in self._products:
            if product.id == id_:
                return product

        raise RuntimeError(f'Не найден продукт с ID: {id_}')

    def sort_products_by_price(self) -> None:
        self._products.sort(key=lambda x: x.cost)

    def get_most_expensive_product(self) -> Product:
        return max(self._products, key=lambda x: x.cost)


class Cart:
    def __init__(self, shop: Shop):
        self._shop = shop
        self._total_price = 0
        self._cart_items = []

    @property
    def total_price(self):
        return self._total_price

    def add_product_by_id(self, id_: int) -> None:
        product = self._get_product_by_id_from_shop(id_)
        self._add_product(product)
        self._recalculate()

    def _recalculate(self) -> None:
        self._total_price = 0
        for product in self._cart_items:
            self._total_price += product.cost * product.quantity

    def _get_product_by_id_from_shop(self, id_: int) -> Product:
        for product in self._shop.products:
            if product.id == id_:
                return product

        raise RuntimeError(f'Не найден продукт с ID: {id_}')

    def _add_product(self, product_from_shop: Product) -> None:
        if product_from_shop.quantity == 0:
            print("Этого товара нет в наличии")
            return

        for product in self._cart_items:
            if product == product_from_shop:
                product.quantity += 1
                break
        else:
            self._cart_items.append(Product(product_from_shop.cost,
                                            product_from_shop.title,
                                            product_from_shop.id,
                                            quantity=1))

        product_from_shop.quantity -= 1
        self._recalculate()

    def remove_product_by_id(self, id_: int) -> None:
        for product in self._cart_items:
            if product.id == id_:
                product.quantity -= 1
                if product.quantity == 0:
                    self._cart_items.remove(product)
                break
        else:
            raise RuntimeError(f'В корзине не найден товар с ID: {id_}')

        self._recalculate()
        product_from_shop = self._get_product_by_id_from_shop(id_)
        product_from_shop.quantity += 1

    def print_cart_items(self) -> None:
        form = '{:>3}|{:<20}|{:<9}|{:<3}'
        print('Сейчас у вас в корзине:')
        print(form.format("ID", "Название", "Цена, р.", "Кол-во в корзине, шт."))
        for product in self._cart_items:
            print(form.format(product.id, product.title, product.cost, product.quantity))
        print(f'Общая стоимость корзины: {self._total_price} р.\n')
