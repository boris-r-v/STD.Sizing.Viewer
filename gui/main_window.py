# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.objects_view = QtWidgets.QTreeWidget(self.splitter_4)
        self.objects_view.setObjectName("objects_view")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.chart_view = PlotWidget(self.splitter_3)
        self.chart_view.setObjectName("chart_view")
        self.table_view = QtWidgets.QTableWidget(self.splitter_3)
        self.table_view.setColumnCount(3)
        self.table_view.setObjectName("table_view")
        self.table_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_view.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.splitter_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.objects_view.headerItem().setText(0, _translate("MainWindow", "Объекты измерений"))
        item = self.table_view.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Время"))
        item = self.table_view.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Значение"))
        item = self.table_view.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Состояние"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
