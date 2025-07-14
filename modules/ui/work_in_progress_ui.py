from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class WorkInProgressUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Work In Progress", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Input fields
        form_layout = QHBoxLayout()
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Product Name")
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Quantity in Progress")
        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Status (e.g., Mixing, Drying)")
        self.worker_input = QLineEdit()
        self.worker_input.setPlaceholderText("Assigned Worker")

        form_layout.addWidget(self.product_input)
        form_layout.addWidget(self.quantity_input)
        form_layout.addWidget(self.status_input)
        form_layout.addWidget(self.worker_input)

        layout.addLayout(form_layout)

        # Button
        self.add_button = QPushButton("Add to WIP")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        layout.addWidget(self.add_button)

        # Table
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Product", "Quantity", "Status", "Worker"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect logic
        self.add_button.clicked.connect(self.add_wip_entry)

    def add_wip_entry(self):
        product = self.product_input.text()
        quantity = self.quantity_input.text()
        status = self.status_input.text()
        worker = self.worker_input.text()

        if product and quantity and status and worker:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(product))
            self.table.setItem(row, 1, QTableWidgetItem(quantity))
            self.table.setItem(row, 2, QTableWidgetItem(status))
            self.table.setItem(row, 3, QTableWidgetItem(worker))

            self.product_input.clear()
            self.quantity_input.clear()
            self.status_input.clear()
            self.worker_input.clear()
