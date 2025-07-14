from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import Qt

class OrdersUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Orders", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Input Fields
        form_layout = QHBoxLayout()

        self.customer_input = QLineEdit()
        self.customer_input.setPlaceholderText("Customer Name")

        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Product Ordered")

        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Quantity")

        self.status_combo = QComboBox()
        self.status_combo.addItems(["Pending", "In Progress", "Completed"])

        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Low", "Medium", "High"])

        form_layout.addWidget(self.customer_input)
        form_layout.addWidget(self.product_input)
        form_layout.addWidget(self.quantity_input)
        form_layout.addWidget(self.status_combo)
        form_layout.addWidget(self.priority_combo)

        layout.addLayout(form_layout)

        # Button
        self.add_button = QPushButton("Add Order")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        layout.addWidget(self.add_button)

        # Table
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Customer", "Product", "Quantity", "Status", "Priority"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect logic
        self.add_button.clicked.connect(self.add_order)

    def add_order(self):
        customer = self.customer_input.text()
        product = self.product_input.text()
        quantity = self.quantity_input.text()
        status = self.status_combo.currentText()
        priority = self.priority_combo.currentText()

        if customer and product and quantity:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(customer))
            self.table.setItem(row, 1, QTableWidgetItem(product))
            self.table.setItem(row, 2, QTableWidgetItem(quantity))
            self.table.setItem(row, 3, QTableWidgetItem(status))
            self.table.setItem(row, 4, QTableWidgetItem(priority))

            self.customer_input.clear()
            self.product_input.clear()
            self.quantity_input.clear()
