from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from Views.ProductList import ProductList

class MainWindow:
    def __init__(self):
        self.widget = self.createWidget()

        self.product_list = ProductList()

    def show(self):
        self.widget.showFullScreen()

    def hide(self):
        self.widget.hide()

    def handleComprarButton(self):
        self.product_list.show()

    def handleSaldoButton(self):
        print(" asass ")

    def createWidget(self):
        widget = QWidget()
        widget.setGeometry(QRect(0, 0, 640, 480))
        widget.setCursor(Qt.BlankCursor)

        shape = QDesktopWidget().screenGeometry()
        width = shape.width()
        height = shape.height()

        grid = QGridLayout(widget)

        bg = QLabel(widget)
        bg.setPixmap(QPixmap("assets/background.jpg"))
        bg.resize(width, height)
        bg.setAlignment(Qt.AlignCenter)

        pic = QLabel()
        image = QPixmap("assets/logo.png")
        pixmap_resized = image.scaled(256, 256, Qt.KeepAspectRatio)
        pic.setPixmap(pixmap_resized)
        pic.setStyleSheet("width: 30px")
        pic.setAlignment(Qt.AlignCenter)


        # Add a button
        btn = QPushButton('Comprar')
        btn.clicked.connect(self.handleComprarButton)
        btn.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)
        btn.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 25px; font-weight: bold; color: white")

        # Add a button
        btn2 = QPushButton('Saldo')
        btn2.clicked.connect(self.handleSaldoButton)
        btn2.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)
        btn2.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 25px; font-weight: bold; color: white")

        grid.addWidget(pic, 0, 0)
        grid.addWidget(btn, 1, 0)
        grid.addWidget(btn2, 2, 0)

        return widget
