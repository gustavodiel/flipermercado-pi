import sys
import sip

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from product_model import Product

from Views.MainWindow import MainWindow


if __name__ == "__main__":

    app = QApplication([])

    main_widget = MainWindow()

    main_widget.show()
    app.exec_()
