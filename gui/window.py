from main_window import Ui_MainWindow
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


