from helpers import api_handler


class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    @staticmethod
    def get_products(category):
        result = api_handler.fetch_all_products()
        if not category:
            return result

        for i in result:
            print(i)
