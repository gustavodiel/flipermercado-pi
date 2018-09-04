from models.product_model import Product
from helpers import api_handler

class Category:

    def __init__(self, name, products=None):
        if products is None:
            products = []

        self.name = name
        self.products = products

    @staticmethod
    def get_categories():
        # Fetch from server

        categorias = api_handler.fetch_all_categories()

        ret = []

        for query in categorias:
            name = query['category']
            categoria = Category(name, Product.get_products(name))

            ret.append(categoria)

        return ret
