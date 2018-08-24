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
            Category("Bebidas",
                     [Product(3.32, 'AGUA COM SAL'), Product(4.50, 'AGUA NORMAL'), Product(8.90, 'AGUA SEM GAS'),
                      Product(23, 'Coca Cola'), Product(1, 'IPA'), Product(0, "MONSTER"),
                      Product(23, 'MONSTER verde'), Product(1, 'Guarana'), Product(0, "Laranjinha")]),
            Category("Bolachas/Biscoitos",
                     [Product(6, 'Trakinas'), Product(4.50, 'Oreo'), Product(4.10, 'Bolacha Cartoon')]),
            Category("Salgados", [Product(1.32, 'EQUILIBRIIIII'), Product(2.52, 'Doritos'), Product(1.90, 'Ruffles <3'),
                                  Product(23, 'Biluzitos'), Product(66.99, 'Xablau')])]
