import requests

from models.product_model import Product


class Category:

    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    @staticmethod
    def get_categories():
        # Fetch from server

        return [
            Category("Bebidas", Product.get_products("Bebidas")),
            Category("Bolachas/Biscoitos", Product.get_products("Bolachas")),
            Category("Salgados", Product.get_products("Salgados"))]
