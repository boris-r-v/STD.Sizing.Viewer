from main_window import Ui_MainWindow
from PyQt5 import QtWidgets
from sizing_data import Pool
import sqlite_driver
from typing import List





class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.pool = None
        self.setupUi(self)
        self.objects_view.itemDoubleClicked.connect(self.handle_item_double_clicked)
        self.sizing = None
        self.table_view.setColumnWidth(0, 200)
        self.table_view.setColumnWidth(2, 100)


    def load_pool(self, pool: Pool) -> None:
        self.pool = pool
        for obj in pool.objects.values():
            top_level_tree_item = QtWidgets.QTreeWidgetItem()
            top_level_tree_item.setText(0, obj.name)
            for src in obj.sources.values():
                child_tree_item = QtWidgets.QTreeWidgetItem()
                child_tree_item.setText(0, src.name)
                top_level_tree_item.addChild(child_tree_item)
            self.objects_view.addTopLevelItem(top_level_tree_item)

    def handle_item_double_clicked(self, child: QtWidgets.QTreeWidgetItem) -> None:
        parent = child.parent()
        if parent is not None:
            from datetime import datetime
            sizing = self.pool.objects[parent.text(0)].sources[child.text(0)].sizing
            self.sizing = (parent.text(0), child.text(0))
            # fill sizing table
            self.table_view.setRowCount(0)
            values: List[float] = []
            times: List[str] = []
            for data in sizing:
                n_row: int = self.table_view.rowCount()
                self.table_view.insertRow(n_row)
                times.append(datetime.utcfromtimestamp(data.sec).strftime('%H:%M:%S'))
                self.table_view.setItem(n_row, 0, QtWidgets.QTableWidgetItem(
                                    datetime.utcfromtimestamp(data.sec).strftime('%Y-%m-%d %H:%M:%S')))
                self.table_view.setItem(n_row, 1, QtWidgets.QTableWidgetItem(str(data.value)))
                mnemo_state_str: str=u"Свободна"
                if 1==data.mnemo_state:
                    mnemo_state_str = u"Занята"
                self.table_view.setItem(n_row, 2, QtWidgets.QTableWidgetItem(mnemo_state_str))
                values.append(data.value)
            #draw graph
            self.graphic_view.canvas.axes.clear()
            self.graphic_view.canvas.axes.tick_params(axis='x', rotation=40)
            #self.graphic_view.canvas.axes.plot(list(range(0,len(values))), values)
            #self.graphic_view.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
            self.graphic_view.canvas.axes.set_title(f'{self.sizing[0]} - {self.sizing[1]}')

            self.graphic_view.canvas.axes.plot(times, values)
            self.graphic_view.canvas.draw()




    def clear_all(self) -> None:
        if self.pool is not None:
            self.table_view.clear()
            self.table_view.setRowCount(0)
            self.objects_view.clear()
            self.pool.clear()
            self.sizing = None

    def open_file_chooser_dialog(self) -> str:
        import os
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Open log database", os.getcwd(),
                                                     "STD sizing log(*.sqlite.db)")
        return path[0]

    def open_data_base_signal_handle(self) -> None:
        self.clear_all()
        path = self.open_file_chooser_dialog()
        self.load_pool(sqlite_driver.get_pool(path))
        pass

    def save_to_cvs_signal_handle(self) -> None:
        if self.sizing is not None:
            import os
            path = QtWidgets.QFileDialog.getSaveFileName(self, "Export to CSV", os.getcwd() + "/data.csv", "csv(*.csv)")
            csv = open(path[0], "w")
            csv.write("index;value;rc_state\n")
            index: int = 0
            for data in self.pool.objects[self.sizing[0]].sources[self.sizing[1]].sizing:
                index += 1
                csv.write(f"{index};{str(data.value)};{data.mnemo_state}\n")
            csv.close()
        else:
            self.show_dialog("Информация", "Експорт невозможен:\n - данные не выбраны, нечего экпортировать")

    @staticmethod
    def show_dialog(title, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg_box.exec()
      
