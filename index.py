import sys

import sip

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from product_model import Product

from Views.MainWindow import MainWindow


if __name__ == "__main__":

    app = QApplication([])

    main_widget = MainWindow()

    main_widget.show()
    app.exec_()
