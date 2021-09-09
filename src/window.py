from src.main_window import Ui_MainWindow
from PyQt5 import QtWidgets
from sizing_data import Pool

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.objects_view.itemDoubleClicked.connect(self.handle_item_double_clicked)

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
            print(parent.text(0), child.text(0))
            sizing = self.pool.objects[parent.text(0)].sources[child.text(0)].sizing
            for i in sizing:
                print (i)

