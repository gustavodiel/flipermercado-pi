from functools import partial

from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
        button = QPushButton("Deseja realmente comprar?", self.widget)
        button.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 2px solid white; font-size: 25px; font-weight: bold; color: white")
        button.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)
        button.move(self.width/2,self.height/2)
        button.show()

    def createWidget(self):
        widget = QWidget()
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
