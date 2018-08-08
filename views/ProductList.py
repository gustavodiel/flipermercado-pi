from functools import partial

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from product_model import Product

class PopupWidget(QWidget):
    def __init__(self, parent_widget, product):
        QWidget.__init__(self)
        self.parent_widget = parent_widget

        self.seconds_remaining = 15

        self.product = product

        shape = QDesktopWidget().screenGeometry()
        self.width = shape.width()
        self.height = shape.height()

        self.bg = QLabel(self)
        self.bg.setStyleSheet("background-color: rgba(0, 0, 0, 200);")
        self.bg.setGeometry(0, 0, self.width, self.height)
        self.bg.setAlignment(Qt.AlignCenter)


        grid = QGridLayout(self)

        # Are you sure you wanna buy? label
        self.are_you_sure_label = QLabel("Passe o seu token RFDI para comprar '{}' por R${}?\n{}s".format(self.product.name, self.product.price, self.seconds_remaining))
        self.are_you_sure_label.setAlignment(Qt.AlignCenter)
        self.are_you_sure_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 24px; font-weight: bold; color: white")

        # No button
        self.no_button = QPushButton("Cancelar")
        self.no_button.clicked.connect(self.handleCancelPurchase)
        self.no_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 32px; font-weight: bold; color: white")

        # Add the
        grid.addWidget(self.are_you_sure_label, 0, 0, 1, 2)
        grid.addWidget(self.no_button, 1, 0, 2, 2)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000) #trigger every second.

    def update(self):
        if self.are_you_sure_label == 0:
            self.close()
            
        self.seconds_remaining -= 1
        self.are_you_sure_label.setText("Passe o seu token RFDI para comprar '{}' por R${}?\n{}s".format(self.product.name, self.product.price, self.seconds_remaining))

    def closeEvent(self, event):
        self.parent_widget.setGraphicsEffect(None)
        event.accept()

    def handleCancelPurchase(self):
        self.close()

class ProductList:
    ''' Controlls the product list view, and the objects '''

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
        self.popup = PopupWidget(self.widget, product)
        # self.popup.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint);
        # self.popup.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.popup.setAttribute(Qt.WA_NoSystemBackground, True)

        self.widget.setGraphicsEffect(QGraphicsBlurEffect())

        self.popup.showFullScreen()

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
