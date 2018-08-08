from PyQt4.QtGui import *
from PyQt4.QtCore import *

from views.ProductList import ProductList

class MainWindow:
    """ Initiates the main application and the window view """

    def __init__(self):
        self.widget = self.createWidget()
        self.product_list = ProductList()

    ''' Shows the main widget '''
    def show(self):
        self.widget.showFullScreen()

    ''' Hides the main widget '''
    def hide(self):
        self.widget.hide()

    ''' Whenever the Comprar button is pressed '''
    def handleComprarButton(self):
        self.product_list.show()

    ''' Whenever the user presses Saldo button '''
    def handleSaldoButton(self):
        print(" asass ")

    ''' Creates the main widget '''
    def createWidget(self):
        widget = QWidget()

        # This disables the cursor
        widget.setCursor(Qt.BlankCursor)

        # Because we want to adapt to the screen, we take it's shape
        shape = QDesktopWidget().screenGeometry()
        width = shape.width()
        height = shape.height()

        # We use the Grid to better space our objects, easly
        grid = QGridLayout(widget)

        # Background
        bg = QLabel(widget)
        bg.setPixmap(QPixmap("assets/background.jpg"))
        bg.resize(width, height)
        bg.setAlignment(Qt.AlignCenter)

        # Logo picture up top
        pic = QLabel()
        image = QPixmap("assets/logo.png")
        pixmap_resized = image.scaled(256, 256, Qt.KeepAspectRatio)
        pic.setPixmap(pixmap_resized)
        pic.setStyleSheet("width: 30px")
        pic.setAlignment(Qt.AlignCenter)


        # Comprar button
        btn = QPushButton('Comprar')
        btn.clicked.connect(self.handleComprarButton)
        btn.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)
        btn.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 28px; font-weight: bold; color: white")

        # Sald button
        btn2 = QPushButton('Saldo')
        btn2.clicked.connect(self.handleSaldoButton)
        btn2.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred)
        btn2.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 28px; font-weight: bold; color: white")

        # Add all the widgets to the grid view
        grid.addWidget(pic, 0, 0)
        grid.addWidget(btn, 1, 0)
        grid.addWidget(btn2, 2, 0)

        return widget
