from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QToolBar, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import sys

# Import your module UIs here
from modules.raw_materials_ui import RawMaterialsUI
from modules.finished_goods_ui import FinishedGoodsUI
from modules.order_ui import OrdersUI 
from modules.packing_ui import PackingUI
from modules.reports_ui import ReportsUI
from modules.machines_ui import MachinesUI
from modules.work_in_progress_ui import WorkProgressUI
from modules.wages_ui import WagesUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Archive by VA")
        self.setFixedSize(1200, 750)

        # Central widget using QStackedWidget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Instantiate and add each module to the stack
        self.raw_materials_ui = RawMaterialsUI()
        self.finished_goods_ui = FinishedGoodsUI()
        self.orders_ui = OrdersUI()
        self.packing_ui = PackingUI()
        self.reports_ui = ReportsUI()
        self.machines_ui = MachinesUI()
        self.work_progress_ui = WorkProgressUI()
        self.wages_ui = WagesUI()

        self.stack.addWidget(self.raw_materials_ui)
        self.stack.addWidget(self.finished_goods_ui)
        self.stack.addWidget(self.orders_ui)
        self.stack.addWidget(self.packing_ui)
        self.stack.addWidget(self.reports_ui)
        self.stack.addWidget(self.machines_ui)
        self.stack.addWidget(self.work_progress_ui)
        self.stack.addWidget(self.wages_ui)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)

        # Toolbar Actions
        self.add_toolbar_action(toolbar, "Raw Materials", self.raw_materials_ui)
        self.add_toolbar_action(toolbar, "Finished Goods", self.finished_goods_ui)
        self.add_toolbar_action(toolbar, "Orders", self.orders_ui)
        self.add_toolbar_action(toolbar, "Packing", self.packing_ui)
        self.add_toolbar_action(toolbar, "Reports", self.reports_ui)
        self.add_toolbar_action(toolbar, "Machines", self.machines_ui)
        self.add_toolbar_action(toolbar, "Work Progress", self.work_progress_ui)
        self.add_toolbar_action(toolbar, "Wages", self.wages_ui)

    def add_toolbar_action(self, toolbar, name, widget):
        action = QAction(QIcon(), name, self)
        action.triggered.connect(lambda: self.stack.setCurrentWidget(widget))
        toolbar.addAction(action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
