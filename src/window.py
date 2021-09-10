from src.main_window import Ui_MainWindow
from PyQt5 import QtWidgets
from sizing_data import Pool
import sqlite_driver

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.objects_view.itemDoubleClicked.connect(self.handle_item_double_clicked)
        self.sizing = None

    def load_pool(self, pool: Pool) -> None:
        self.pool = pool
        for obj in pool.objects.values():
            toplevel_tree_item=QtWidgets.QTreeWidgetItem()
            toplevel_tree_item.setText(0, obj.name)
            for src in obj.sources.values():
                child_tree_item = QtWidgets.QTreeWidgetItem()
                child_tree_item.setText(0, src.name)
                toplevel_tree_item.addChild(child_tree_item)
            self.objects_view.addTopLevelItem(toplevel_tree_item)


    def handle_item_double_clicked(self, child: QtWidgets.QTreeWidgetItem)->None:
        parent = child.parent()
        if parent is not None:
            from datetime import datetime
            sizing = self.pool.objects[parent.text(0)].sources[child.text(0)].sizing
            self.sizing = (parent.text(0), child.text(0))
            print (self.sizing)
            self.table_view.clear()
            self.table_view.setRowCount(0)
            for data in sizing:
                nrow:int=self.table_view.rowCount()
                self.table_view.insertRow(nrow)
                self.table_view.setItem(nrow, 0, QtWidgets.QTableWidgetItem(datetime.utcfromtimestamp(data.sec).strftime('%Y-%m-%d %H:%M:%S')))
                self.table_view.setItem(nrow, 1, QtWidgets.QTableWidgetItem(str(data.value)))
                self.table_view.setItem(nrow, 2, QtWidgets.QTableWidgetItem(str(data.mnemo_state)))

    def clear_all(self)->None:
        self.table_view.clear()
        self.table_view.setRowCount(0)
        self.objects_view.clear()
        self.pool.clear()

    def open_file_chooser_dialog(self)->str:
        import os
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Open log database", os.getcwd(), "STD sizing log(*.sqlite.db)")
        return path

    def open_data_base_signal_handle(self)->None:
        self.clear_all()
        path = self.open_file_chooser_dialog()[0]
        self.load_pool(sqlite_driver.get_pool(path))
        pass

    def save_to_cvs_signal_handle(self)->None:
        pass



