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
        MainWindow.resize(890, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setHandleWidth(10)
        self.main_splitter.setChildrenCollapsible(False)
        self.main_splitter.setObjectName("main_splitter")
        self.objects_view = QtWidgets.QTreeWidget(self.main_splitter)
        self.objects_view.setMinimumSize(QtCore.QSize(0, 0))
        self.objects_view.setObjectName("objects_view")
        self.chart_sizing_splitter = QtWidgets.QSplitter(self.main_splitter)
        self.chart_sizing_splitter.setOrientation(QtCore.Qt.Vertical)
        self.chart_sizing_splitter.setHandleWidth(10)
        self.chart_sizing_splitter.setChildrenCollapsible(True)
        self.chart_sizing_splitter.setObjectName("chart_sizing_splitter")
        self.table_view = QtWidgets.QTableWidget(self.chart_sizing_splitter)
        self.table_view.setMinimumSize(QtCore.QSize(30, 220))
        self.table_view.setColumnCount(3)
        self.table_view.setObjectName("table_view")
        self.table_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_view.setHorizontalHeaderItem(2, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.chart_sizing_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graphis_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graphis_layout.setContentsMargins(0, 0, 0, 0)
        self.graphis_layout.setObjectName("graphis_layout")
        self.graphic_view = MplWidget(self.verticalLayoutWidget)
        self.graphic_view.setObjectName("graphic_view")
        self.graphis_layout.addWidget(self.graphic_view)
        self.verticalLayout.addWidget(self.main_splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 890, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_sqlite_db = QtWidgets.QAction(MainWindow)
        self.actionOpen_sqlite_db.setObjectName("actionOpen_sqlite_db")
        self.actionExport_to_csv = QtWidgets.QAction(MainWindow)
        self.actionExport_to_csv.setObjectName("actionExport_to_csv")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_sqlite_db)
        self.menuFile.addAction(self.actionExport_to_csv)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpen_sqlite_db.triggered.connect(MainWindow.open_data_base_signal_handle)
        self.actionExport_to_csv.triggered.connect(MainWindow.save_to_cvs_signal_handle)
        self.actionExit.triggered.connect(MainWindow.close)
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
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_sqlite_db.setText(_translate("MainWindow", "Open sqlite.db"))
        self.actionOpen_sqlite_db.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExport_to_csv.setText(_translate("MainWindow", "Export sizing to csv"))
        self.actionExport_to_csv.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
