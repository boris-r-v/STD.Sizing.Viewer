from unittest import TestCase
from window import Window
from PyQt5 import QtWidgets

class TestWindow(TestCase):
    def test_init(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        win = Window()
        win.show()
        app.exec_()
        self.assertTrue(True)
