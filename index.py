from PyQt4.QtGui import *

from views.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    main_widget = MainWindow()

    main_widget.show()
    app.exec_()
