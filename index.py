import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sip

### Show Memory usage ###
import os
import psutil
process = psutil.Process(os.getpid())

main_widget = None
comprar_widget = None

def handleComprar():
    comprar_widget.showFullScreen()

def handleSaldo():
    print("Not implemented")

def handleMemory():
    main_widget.showFullScreen()

def createMainWidget():
    global main_widget
    main_widget = QWidget()
        # w.setStyleSheet("background: url(background.jpg) center;")
    shape = QDesktopWidget().screenGeometry()
    width = shape.width()
    height = shape.height()

    grid = QGridLayout(main_widget)

    bg = QLabel(main_widget)
    bg.setPixmap(QPixmap("background.jpg"))
    bg.resize(width, height)
    bg.setAlignment(Qt.AlignCenter)

    pic = QLabel()
    pic.setPixmap(QPixmap("logo.png"))
    pic.resize(300, 300)
    pic.setAlignment(Qt.AlignCenter)


    # Add a button
    btn = QPushButton('Comprar')
    btn.clicked.connect(handleComprar)
    btn.setSizePolicy(
        QSizePolicy.Preferred,
        QSizePolicy.Preferred)
    btn.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 25px; font-weight: bold; color: white")

    # Add a button
    btn2 = QPushButton('Saldo')
    btn2.clicked.connect(handleSaldo)
    btn2.setSizePolicy(
        QSizePolicy.Preferred,
        QSizePolicy.Preferred)
    btn2.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 25px; font-weight: bold; color: white")

    grid.addWidget(pic, 0, 0)
    grid.addWidget(btn, 1, 0)
    grid.addWidget(btn2, 2, 0)

def createComprarWidget():
    global comprar_widget
    comprar_widget = QWidget()
        # w.setStyleSheet("background: url(background.jpg) center;")
    shape = QDesktopWidget().screenGeometry()
    width = shape.width()
    height = shape.height()

    grid = QGridLayout(comprar_widget)

    bg = QLabel(comprar_widget)
    bg.setPixmap(QPixmap("background.jpg"))
    bg.resize(width, height)
    bg.setAlignment(Qt.AlignCenter)


    # Add a button
    for i in range(5):
        for k in range(5):
            btn = QPushButton('Botao {}:{}'.format(i, k))
            btn.clicked.connect(handleMemory)
            btn.setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Preferred)
            btn.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none; font-size: 25px; font-weight: bold; color: white")

            grid.addWidget(btn, i, k)

def handleSaldo():
    print("Saldooo")


if __name__ == "__main__":
    app = QApplication([])

    createMainWidget()
    createComprarWidget()

    main_widget.showFullScreen()
    app.exec_()
