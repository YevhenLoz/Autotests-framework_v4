from prettytable import PrettyTable
import sys
from pony.orm import db_session, left_join
from hw_13.db.models.models import Products
import os
import webbrowser


class ProductRepository:
    def __init__(self):
        self.__model = Products

    @db_session
    def add_product(self, name, price):
        self.__model(name=name, price=price)

    @db_session
    def left_join(self, original_stdout=sys.stdout):
        with open('join.csv', 'w') as f:
            sys.stdout = f
            results = left_join((products, orders) for products in self.__model for orders in
                                products.orders)
            print("id", "name", "price", "quantity", "total", sep=",", file=f)
            for result in results:
                products = result[0]
                orders = result[1]
                print(f"{products.id}, {products.name}, {products.price}, {orders.quantity},"
                      f"{products.price * orders.quantity}", file=f)
                sys.stdout = original_stdout

        to_csv = open('join.csv', 'r')
        to_csv = to_csv.readlines()
        tab_data = to_csv[0]
        tab_data = tab_data.split(",")
        table = PrettyTable([tab_data[0], tab_data[1], tab_data[2], tab_data[3], tab_data[4]])
        for i in range(1, len(to_csv)):
            table.add_row(to_csv[i].split(','))
        code = table.get_html_string()
        html_file = open('Table.html', 'w')
        html_file.write(code)
        filename = 'file:///' + os.getcwd() + '/' + 'Table.html'
        webbrowser.open_new_tab(filename)


if __name__ == '__main__':
    product_repo = ProductRepository()
    # product_repo.add_product('iPhone13 Pro', 1000)
    # product_repo.add_product('Samsung Galaxy 22', 900)
    # product_repo.add_product('Xiaomi 11T', 300)
    # product_repo.add_product('Nokia 1100', 10)
    # product_repo.add_product('Motorola X', 50)
    product_repo.left_join()
