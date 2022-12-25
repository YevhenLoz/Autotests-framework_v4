from pony.orm import Database, PrimaryKey, Required, Set, Optional

db = Database()
db.bind('postgres', user='postgres', password='Leki@2022', host='127.0.0.1', database='mytestbase')


class Products(db.Entity):
    __table__ = "products"
    id = PrimaryKey(int, auto=True)
    name = Required(str, 25)
    price = Optional(float)
    orders = Set("Orders")


class Orders(db.Entity):
    __table__ = "orders"
    id = PrimaryKey(int, auto=True)
    quantity = Required(int)
    products = Required(Products, column="product_id")


db.generate_mapping(create_tables=False)
