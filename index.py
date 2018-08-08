import sys

import sip

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from product_model import Product

from views.MainWindow import MainWindow


if __name__ == "__main__":

    app = QApplication([])

    main_widget = MainWindow()

    main_widget.show()
    app.exec_()
