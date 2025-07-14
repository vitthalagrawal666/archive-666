from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
import sys

# Import all module screens
from modules.raw_materials import RawMaterialScreen
from modules.products import ProductScreen
from modules.orders import OrderScreen
from modules.work_progress import WorkProgressScreen
from modules.machine_tasks import MachineTaskScreen
from modules.packing import PackingScreen
from modules.finished_goods import FinishedGoodsScreen
from modules.wages import WageScreen
from modules.reports import ReportsScreen   # 👈 New import

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Archive by VA - Factory Manager")
        self.setGeometry(100, 100, 1200, 700)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #151515; color: white; font-size: 16px;")
        self.layout.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        self.init_screens()

    def init_screens(self):
        self.screens = {
            "Raw Materials": RawMaterialScreen(),
            "Products": ProductScreen(),
            "Orders": OrderScreen(),
            "Work Progress": WorkProgressScreen(),
            "Machine Tasks": MachineTaskScreen(),
            "Packing": PackingScreen(),
            "Finished Goods": FinishedGoodsScreen(),
            "Wages": WageScreen(),
            "Reports": ReportsScreen(),   # 👈 Add this line
        }

        for name, screen in self.screens.items():
            item = QListWidgetItem(name)
            self.sidebar.addItem(item)
            self.stack.addWidget(screen)

        self.sidebar.currentRowChanged.connect(self.display_screen)
        self.sidebar.setCurrentRow(0)

    def display_screen(self, index):
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
