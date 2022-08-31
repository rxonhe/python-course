class Product:
    """Store Product Info"""
    item_id: int
    item_price: float
    item_name: str

    def __init__(self, item_id, item_price, item_name):
        """
        :param item_id: str
        :param item_price: float
        :param item_name: str
        """
        self.item_id = item_id
        self.item_price = item_price
        self.item_name = item_name

    def __str__(self):
        to_print = """
        Item Name : {self.item_name}
        Item Code: {self.item_id}
        Item Price: {self.item_price}
        """.format(self=self)
        return to_print


class Storage:
    """All products inside the storage"""
    products: list[Product]

    def __init__(self, products):
        """
        :param products: Product
        """
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def __str__(self):
        to_print = "Storage:"
        for product in self.products:
            to_print += "\n" + str(product)
        return to_print


if __name__ == '__main__':
    product_a = Product(1, 10.99, "Product A")
    product_b = Product(1, 12.99, "Product B")
    product_c = Product(1, 13.99, "Product C")

    print("Product A price: {}".format(product_a.item_price))

    storage = Storage([product_a, product_b, product_c])

    print(product_a)
    print(storage)
