from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QStackedWidget, QSizePolicy
from PyQt5.QtCore import Qt

# Import all UI modules
from ui.raw_materials_ui import RawMaterialUI
from ui.work_in_progress_ui import WorkProgressUI
from ui.order_ui import OrdersUI
from ui.machines_ui import MachinesUI
from ui.packing_ui import PackingUI
from ui.finished_goods_ui import FinishedGoodsUI
from ui.wages_ui import WagesUI
from ui.reports_ui import ReportsUI
from ui.backup_restore_ui import BackupRestoreUI

class DashboardUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        main_layout = QHBoxLayout(self)

        # Sidebar layout for navigation
        sidebar = QVBoxLayout()
        sidebar.setAlignment(Qt.AlignTop)

        self.stack = QStackedWidget(self)

        # Buttons and corresponding screens
        self.screens = {
            "Raw Materials": RawMaterialUI(),
            "Work Progress": WorkProgressUI(),
            "Orders": OrdersUI(),
            "Machines": MachinesUI(),
            "Packing": PackingUI(),
            "Finished Goods": FinishedGoodsUI(),
            "Wages": WagesUI(),
            "Reports": ReportsUI(),
            "Backup": BackupRestoreUI()
        }

        # Add buttons and screens
        for name, widget in self.screens.items():
            btn = QPushButton(name)
            btn.setStyleSheet(self.button_style())
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda checked, name=name: self.load_screen(name))
            sidebar.addWidget(btn)
            self.stack.addWidget(widget)

        # Layout setup
        main_layout.addLayout(sidebar, 1)
        main_layout.addWidget(self.stack, 4)

        # Load default screen
        self.load_screen("Raw Materials")

    def load_screen(self, name):
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            if isinstance(widget, type(self.screens[name])):
                self.stack.setCurrentIndex(i)
                break

    def button_style(self):
        return """
            QPushButton {
                background-color: #333333;
                color: white;
                padding: 12px;
                font-size: 14px;
                border-radius: 10px;
                margin-bottom: 8px;
            }
            QPushButton:hover {
                background-color: #0078d7;
            }
        """
