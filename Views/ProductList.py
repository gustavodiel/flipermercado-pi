from functools import partial

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from product_model import Product

class ProductList:
    def __init__(self):
        self.LIMIT_ITEMS_COUNT_X = 5

        shape = QDesktopWidget().screenGeometry()
        self.width = shape.width()
        self.height = shape.height()

        self.products = self.getProducts()
        self.widget = self.createWidget()

    def getProducts(self):
        return [Product(21, 'Banana'),Product(32, 'Maca'),Product(1, 'Hue'),
        Product(42, 'adas'),Product(1, '12312312'),Product(32, 'Maca'),Product(1, 'Hue'),
        Product(42, 'adas'),Product(1, '12312312'),Product(32, 'Maca'),Product(1, 'Hue'),
        Product(42, 'adas'),Product(1, '12312312'),Product(32, 'Maca'),Product(1, 'Hue'),
        Product(42, 'adas'),Product(1, 'LAST'),Product(1, 'LAST')]

    def show(self):
        self.widget.showFullScreen()

    def hide(self):
        self.widget.hide()

    def handleProductPressed(self, product):
        # QMessageBox.about(self.widget, "Hello", "My StackOverflow code was so long that nobody wanted to read it")
        self.popup = QWidget()
        self.popup.setStyleSheet("background-color: rgba(0, 255, 0, 0); border: none; font-size: 25px; font-weight: bold; color: white")
        self.popup.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint);
        self.popup.setAttribute(Qt.WA_TranslucentBackground, True)
        self.popup.setAttribute(Qt.WA_NoSystemBackground, True)
        self.popup.setAttribute(Qt.WA_PaintOnScreen, True)
        self.popup.setGeometry(QRect(100, 100, 400, 200))
            # w.setStyleSheet("background: url(background.jpg) center;")
        grid = QGridLayout(self.popup)

        buttonLabel = "Deseja realmente comprar '{}' por R${}?".format(product.name, product.price)
        button = QLabel(buttonLabel)
        button.setAlignment(Qt.AlignCenter)
        button.setStyleSheet("background-color: rgba(0, 0, 0, 150); border: none; font-size: 25px; font-weight: bold; color: white")

        grid.addWidget(button, 0, 0)

        btnYes = QLabel("Sim")
        btnYes.setStyleSheet("background-color: rgba(0, 0, 0, 150); border: none; font-size: 25px; font-weight: bold; color: white")

        grid.addWidget(button, 1, 0)


        btnNo = QLabel("Nao")
        btnNo.setStyleSheet("background-color: rgba(0, 0, 0, 150); border: none; font-size: 25px; font-weight: bold; color: white")

        grid.addWidget(button, 1, 1)

        self.popup.show()

    def createWidget(self):
        widget = QWidget()
        widget.setCursor(Qt.BlankCursor)
            # w.setStyleSheet("background: url(background.jpg) center;")

        grid = QGridLayout(widget)

        bg = QLabel(widget)
        bg.setPixmap(QPixmap("assets/background.jpg"))
        bg.resize(self.width, self.height)
        bg.setAlignment(Qt.AlignCenter)

        # Add a button
        posX = 0
        posY = 0
        for i in self.products:
            btn = QPushButton(i.name + '\n' + 'R$' + str(i.price))
            btn.clicked.connect(partial(self.handleProductPressed, i))
            btn.setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Preferred)

            btn.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 25px; font-weight: bold; color: white")

            grid.addWidget(btn, posY, posX)
            posX += 1

            if posX > self.LIMIT_ITEMS_COUNT_X:
                posX = 0
                posY += 1

        return widget
