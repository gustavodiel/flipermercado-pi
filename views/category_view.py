from functools import partial

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from models.category_model import Category

from views.ProductList import ProductList
from models.product_model import Product


class CategoryView(QWidget):
    ''' Controlls the product list view, and the objects '''

    def __init__(self):
        QWidget.__init__(self)
        self.LIMIT_ITEMS_COUNT_X = 5

        self.product_list = None

        shape = QDesktopWidget().screenGeometry()
        self.width = shape.width()
        self.height = shape.height()

        self.categories = self.get_categories()
        self.widget = QWidget()
        self.grid = QGridLayout(self.widget)
        self.createWidget()

    def get_categories(self):
        return Category.get_categories()

    def show(self):
        self.widget.showFullScreen()

    def hide(self):
        self.widget.hide()

    def handle_category_pressed(self, category):
        self.product_list = ProductList(Product.get_products(category.name), self)
        self.product_list.show()

    def handle_back_button_pressed(self):
        self.hide()

    def reload_data(self):
        self.categories = self.get_categories()
        self.createWidget()

    def createWidget(self):

        while self.grid.count():
            child = self.grid.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()

        bg = QLabel(self.widget)
        bg.setPixmap(QPixmap("assets/background.jpg"))
        bg.resize(self.width, self.height)
        bg.setAlignment(Qt.AlignCenter)

        # Add a button
        posX = 0
        posY = 0
        for i in self.categories:
            btn = QPushButton('{}\n{}'.format(i.name, len(i.products)))
            btn.clicked.connect(partial(self.handle_category_pressed, i))
            btn.setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Preferred)

            btn.setStyleSheet(
                "background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 22px; font-weight: bold; color: white")

            self.grid.addWidget(btn, posY, posX, 2, 1)
            posX += 1

            if posX > self.LIMIT_ITEMS_COUNT_X:
                posX = 0
                posY += 1

        button_back = QPushButton('Voltar')
        button_back.clicked.connect(self.handle_back_button_pressed)
        button_back.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)

        button_back.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 28px; font-weight: bold; color: white")

        self.grid.addWidget(button_back, 2, 0, 1, -1)
