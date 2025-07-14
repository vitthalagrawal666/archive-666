from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
import sqlite3
from datetime import datetime

class PackingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packing Management")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()
        self.load_packing_data()

    def init_ui(self):
        title = QLabel("Packing Material Usage")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Material", "Quantity Used", "Cost", "Date"])
        self.layout.addWidget(self.table)

        input_layout = QHBoxLayout()
        self.material_input = QLineEdit()
        self.material_input.setPlaceholderText("Packing Material")
        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Quantity")
        self.cost_input = QLineEdit()
        self.cost_input.setPlaceholderText("Cost")
        input_layout.addWidget(self.material_input)
        input_layout.addWidget(self.qty_input)
        input_layout.addWidget(self.cost_input)
        self.layout.addLayout(input_layout)

        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Entry")
        add_btn.clicked.connect(self.add_packing_entry)
        btn_layout.addWidget(add_btn)
        self.layout.addLayout(btn_layout)

        self.setStyleSheet("QWidget { background-color: #1e1e1e; color: white; } QPushButton { background-color: #007acc; color: white; padding: 5px 10px; }")

    def load_packing_data(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS packing (
            material TEXT, quantity INTEGER, cost REAL, date TEXT
        )""")
        c.execute("SELECT * FROM packing")
        records = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()

    def add_packing_entry(self):
        material = self.material_input.text()
        try:
            quantity = int(self.qty_input.text())
            cost = float(self.cost_input.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Quantity must be an integer and Cost must be a number.")
            return

        date = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("INSERT INTO packing VALUES (?, ?, ?, ?)", (material, quantity, cost, date))
        conn.commit()
        conn.close()
        self.load_packing_data()

        self.material_input.clear()
        self.qty_input.clear()
        self.cost_input.clear()
