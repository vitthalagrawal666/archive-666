from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class RawMaterialsUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")
        
        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Raw Materials Manager", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Form fields
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Material Name")
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Quantity")
        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("Unit (e.g., kg, L)")
        self.cost_input = QLineEdit()
        self.cost_input.setPlaceholderText("Cost")

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.quantity_input)
        form_layout.addWidget(self.unit_input)
        form_layout.addWidget(self.cost_input)

        layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Material")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        btn_layout.addWidget(self.add_button)

        layout.addLayout(btn_layout)

        # Table
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Name", "Quantity", "Unit", "Cost"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect button
        self.add_button.clicked.connect(self.add_material)

    def add_material(self):
        name = self.name_input.text()
        qty = self.quantity_input.text()
        unit = self.unit_input.text()
        cost = self.cost_input.text()

        if name and qty and unit and cost:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(qty))
            self.table.setItem(row, 2, QTableWidgetItem(unit))
            self.table.setItem(row, 3, QTableWidgetItem(cost))

            self.name_input.clear()
            self.quantity_input.clear()
            self.unit_input.clear()
            self.cost_input.clear()
