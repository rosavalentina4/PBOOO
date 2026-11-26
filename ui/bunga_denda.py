import os
import sys

from PyQt5 import QtWidgets, uic


class BungaDendaWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bunga_denda.ui"), self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BungaDendaWindow()
    window.show()
    sys.exit(app.exec_())
