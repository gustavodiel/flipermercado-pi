import os
import requests

IS_TESTING = True
TEST_URL = 'http://localhost:3050/'


# URL Functions
def server_name():
    """
    Returns the main server URL
    :return: API's URL
    """
    return IS_TESTING and TEST_URL or os.environ['FLIPERMERCADO_SERVER_NAME']


def user_url():
    """
    Returns URL with all users
    :return: API's URL for all users
    """
    return server_name() + 'user'


def products_url():
    """
    Returns URL for all products
    :return: API's URL for all products
    """
    return server_name() + 'products'


# Fetchers
def fetch_all_products():
    request = requests.get(products_url())
    print(request.url)

    return request.json()


def fetch_user(id):
    request = requests.get("{}/{}".format(user_url(), str(id)))
    return request.json()


result = fetch_all_products()
print(list(filter(lambda product: product['price'] > 5, result)))
