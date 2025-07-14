from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class PackingUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Packing Materials Management", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Input Fields
        form_layout = QHBoxLayout()

        self.material_input = QLineEdit()
        self.material_input.setPlaceholderText("Material Name")

        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Quantity Used")

        self.cost_input = QLineEdit()
        self.cost_input.setPlaceholderText("Cost (₹)")

        form_layout.addWidget(self.material_input)
        form_layout.addWidget(self.qty_input)
        form_layout.addWidget(self.cost_input)

        layout.addLayout(form_layout)

        # Button
        self.add_button = QPushButton("Add Material Usage")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        layout.addWidget(self.add_button)

        # Table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Material", "Quantity", "Cost"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect logic
        self.add_button.clicked.connect(self.add_record)

    def add_record(self):
        material = self.material_input.text()
        qty = self.qty_input.text()
        cost = self.cost_input.text()

        if material and qty and cost:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(material))
            self.table.setItem(row, 1, QTableWidgetItem(qty))
            self.table.setItem(row, 2, QTableWidgetItem(cost))

            self.material_input.clear()
            self.qty_input.clear()
            self.cost_input.clear()
