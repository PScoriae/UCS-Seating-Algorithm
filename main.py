from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 250, 500, 500)
    win.setWindowTitle("Seating Algorithm")

    win.show()
    sys.exit(app.exec())

window()