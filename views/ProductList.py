from functools import partial

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from models.category_model import Category
from views.popup_view import PopupView


class ProductList:
    ''' Controlls the product list view, and the objects '''

    def __init__(self, products, main_window):
        self.LIMIT_ITEMS_COUNT_X = 2
        self.LIMIT_ITEMS_COUNT_Y = 1

        shape = QDesktopWidget().screenGeometry()
        self.width = shape.width()
        self.height = shape.height()

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
        for i in self.products:
            btn = QPushButton('{}\nR${:.2f}'.format(i.name, i.price))
            btn.clicked.connect(partial(self.handleProductPressed, i))
            btn.setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Preferred)

            btn.setStyleSheet(
                "background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 18px; font-weight: bold; color: white")

            grid.addWidget(btn, pos_y, pos_x, len(self.products) > self.LIMIT_ITEMS_COUNT_X and 1 or 1, 1)
            pos_x += 1

            if pos_x > self.LIMIT_ITEMS_COUNT_X:
                pos_x = 0
                pos_y += 1
            if pos_y >= self.LIMIT_ITEMS_COUNT_Y:
                pass

        button_back = QPushButton('Voltar')
        button_back.clicked.connect(self.handle_back_button_pressed)
        button_back.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)

        button_back.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 28px; font-weight: bold; color: white")

        grid.addWidget(button_back, round(len(self.products) / self.LIMIT_ITEMS_COUNT_X), 0, 1, -1)

        return widget

    @staticmethod
    def getProducts():
        return Category.get_categories()
