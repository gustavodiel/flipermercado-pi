from helpers import api_handler


class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    @staticmethod
    def get_products(category):
        data = Product.fetch_result(category)
        print(data)
        return [Product(product['price'], product['description']) for product in data]


    @staticmethod
    def fetch_result(category):
        result = api_handler.fetch_products_by_category(category)

        return result
