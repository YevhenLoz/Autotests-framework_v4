from pony.orm import db_session, left_join
from hw_13.db.models.models import Products


class ProductRepository:
    def __init__(self):
        self.__model = Products

    @db_session
    def add_product(self, name, price):
        self.__model(name=name, price=price)

    @db_session
    def left_join(self):
        results = left_join((products, orders) for products in self.__model for orders in products.orders)
        for result in results:
            products = result[0]
            orders = result[1]
            print(f"id: {products.id}, name: {products.name}, price:{products.price} quantity: {orders.quantity}, "
                  f"total: {products.price * orders.quantity}")


if __name__ == '__main__':
    product_repo = ProductRepository()
    # product_repo.add_product('iPhone13 Pro', 1000)
    # product_repo.add_product('Samsung Galaxy 22', 900)
    # product_repo.add_product('Xiaomi 11T', 300)
    # product_repo.add_product('Nokia 1100', 10)
    # product_repo.add_product('Motorola X', 50)
    product_repo.left_join()
