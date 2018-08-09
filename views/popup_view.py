from functools import partial

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from models.product_model import Product

class PopupView(QWidget):
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
        self.are_you_sure_label = QLabel("Passe o seu token RFDI para comprar '{}' por R${:.2f}?\n{}s".format(self.product.name, self.product.price, self.seconds_remaining))
        self.are_you_sure_label.setAlignment(Qt.AlignCenter)
        self.are_you_sure_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 18px; font-weight: bold; color: white")

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
        if self.seconds_remaining <= 0:
            self.close()

        self.seconds_remaining -= 1
        self.are_you_sure_label.setText("Passe o seu token RFDI para comprar '{}' por R${:.2f}?\n{}s".format(self.product.name, self.product.price, self.seconds_remaining))

    def closeEvent(self, event):
        event.accept()

    def handleCancelPurchase(self):
        self.close()
