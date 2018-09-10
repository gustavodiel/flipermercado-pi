from functools import partial
from itertools import zip_longest

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from models.category_model import Category
from views.popup_view import PopupView


class ProductList:
    """ Controlls the product list view, and the objects """

    def __init__(self, products, main_window):
        self.LIMIT_ITEMS_COUNT_X = 3
        self.LIMIT_ITEMS_COUNT_Y = 1

        shape = QDesktopWidget().screenGeometry()
        self.width = shape.width()
        self.height = shape.height()

        self.popup = None

        self.products = products
        self.widget = self.createWidget()

        self.main_window = main_window

    def show(self):
        self.widget.showFullScreen()

    def hide(self):
        self.widget.hide()

    def handleProductPressed(self, product):
        self.popup = PopupView(self.widget, product)
        self.popup.showFullScreen()

    def handle_back_button_pressed(self):
        self.main_window.reload_data()
        self.widget.close()

    def item_len_for_amount(self, amount):
        if amount <= 3:
            return 1

        if amount > self.LIMIT_ITEMS_COUNT_X:
            return 1

    def createWidget(self):
        widget = QWidget()

        grid = QGridLayout(widget)

        bg = QLabel(widget)
        bg.setPixmap(QPixmap("assets/background.jpg"))
        bg.resize(self.width, self.height)
        bg.setAlignment(Qt.AlignCenter)

        # Add a button
        pos_x = 0
        pos_y = 0
        self.products += self.products * 8

        for groups in self.grouper(self.LIMIT_ITEMS_COUNT_X, self.products):
            num_elements_group = len([x for x in groups if x])
            for product in groups:
                if not product or product is None:
                    continue

                btn = QPushButton('{}\nR${:.2f}'.format(product.name, product.price))
                btn.clicked.connect(partial(self.handleProductPressed, product))
                btn.setSizePolicy(
                    QSizePolicy.Preferred,
                    QSizePolicy.Preferred)

                btn.setStyleSheet(
                    "background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 18px; font-weight: bold; color: white")


                # if num_elements_group != self.LIMIT_ITEMS_COUNT_X and pos_y > 0:
                grid.addWidget(btn, pos_y, pos_x, self.item_len_for_amount(len(self.products)), 1)
                print("{} vs {}".format((self.LIMIT_ITEMS_COUNT_X + 1) - num_elements_group, 2 * self.LIMIT_ITEMS_COUNT_X / num_elements_group))
                # else:
                #     grid.addWidget(btn, pos_y, pos_x, self.item_len_for_amount(len(self.products)), 2)
                pos_x += 1

            pos_x = 0
            pos_y += 1

        button_back = QPushButton('Voltar')
        button_back.clicked.connect(self.handle_back_button_pressed)
        button_back.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)

        button_back.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 28px; font-weight: bold; color: white")

        grid.addWidget(button_back, max(round(len(self.products) / self.LIMIT_ITEMS_COUNT_X), 2), 0, 1, -1)

        return widget

    @staticmethod
    def getProducts():
        return Category.get_categories()


    @staticmethod
    def grouper(n, iterable, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)