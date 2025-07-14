from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class FinishedGoodsUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Finished Goods Tracker", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Input section
        form_layout = QHBoxLayout()

        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Product Name")

        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Quantity Finished")

        self.order_id_input = QLineEdit()
        self.order_id_input.setPlaceholderText("Order ID (optional)")

        form_layout.addWidget(self.product_input)
        form_layout.addWidget(self.qty_input)
        form_layout.addWidget(self.order_id_input)

        layout.addLayout(form_layout)

        # Button to add entry
        self.add_button = QPushButton("Add Finished Product")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        layout.addWidget(self.add_button)

        # Table to show finished goods
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Product", "Quantity", "Order ID"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect logic
        self.add_button.clicked.connect(self.add_finished_item)

    def add_finished_item(self):
        product = self.product_input.text()
        qty = self.qty_input.text()
        order_id = self.order_id_input.text()

        if product and qty:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(product))
            self.table.setItem(row, 1, QTableWidgetItem(qty))
            self.table.setItem(row, 2, QTableWidgetItem(order_id))

            self.product_input.clear()
            self.qty_input.clear()
            self.order_id_input.clear()
