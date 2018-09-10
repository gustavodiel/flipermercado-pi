import os
import requests

from requests.auth import HTTPDigestAuth, HTTPBasicAuth
from requests_oauthlib import OAuth1

IS_TESTING = True
TEST_URL = 'http://localhost:3000/'

SERVER_NAME_VARIABLE = 'FLIPERMERCADO_SERVER_NAME'
USER_NAME_VARIABLE = 'FLIPERMERCADO_USER_NAME'
USER_PASSWORD_VARIABLE = 'FLIPERMERCADO_USER_PASS'


# URL Functions
def server_name():
    return IS_TESTING and TEST_URL or os.environ[SERVER_NAME_VARIABLE]


def user_url():
    return server_name() + 'user'


def products_url():
    return server_name() + 'products'


def categories_url():
    return server_name() + 'categories'


# Session helper
def session_request_at_url(session, url):
    session.auth = HTTPBasicAuth(os.environ[USER_NAME_VARIABLE], os.environ[USER_PASSWORD_VARIABLE])

    request = session.get(url)

    if request.status_code == 401:
        raise Exception('Permission Denied to access {} with user: {}'.format(request.url, str(session.auth.username)))

    if request.status_code == 500:
        raise Exception('Server send error code: {}'.format(request.json()))

    return request


# Fetchers
def fetch_all_products():
    session = requests.Session()

    return session_request_at_url(session, products_url()).json()


def fetch_all_categories():
    session = requests.Session()

    return session_request_at_url(session, categories_url()).json()


def fetch_products_by_category(category):
    params = {
        'category': category
    }

    session = requests.Session()
    session.params = params

    return session_request_at_url(session, products_url()).json()



def fetch_user(user_id):
    session = requests.Session()
    url = "{}/{}".format(user_url(), str(user_id))

    return session_request_at_url(session, url)
