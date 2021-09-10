from unittest import TestCase
from window import Window
from PyQt5 import QtWidgets
from sqlite_driver import get_pool

class TestWindow(TestCase):
    def test_init(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        win = Window()
        win.load_pool(get_pool("../tests/test.sqlite.db"))
        win.show()
        app.exec_()
        self.assertTrue(True)

