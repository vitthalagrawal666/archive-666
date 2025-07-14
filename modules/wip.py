from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
import sqlite3
from datetime import datetime

class WIPScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Work In Progress")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()
        self.load_wip_data()

    def init_ui(self):
        title = QLabel("Work In Progress Tracking")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Product", "Quantity", "Status", "Date"])
        self.layout.addWidget(self.table)

        input_layout = QHBoxLayout()
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Product Name")
        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Quantity")
        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Status (e.g. Mixing, Drying)")
        input_layout.addWidget(self.product_input)
        input_layout.addWidget(self.qty_input)
        input_layout.addWidget(self.status_input)
        self.layout.addLayout(input_layout)

        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add WIP Entry")
        add_btn.clicked.connect(self.add_wip_entry)
        btn_layout.addWidget(add_btn)
        self.layout.addLayout(btn_layout)

        self.setStyleSheet("QWidget { background-color: #1e1e1e; color: white; } QPushButton { background-color: #007acc; color: white; padding: 5px 10px; }")

    def load_wip_data(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS wip (
            product TEXT, quantity INTEGER, status TEXT, date TEXT
        )""")
        c.execute("SELECT * FROM wip")
        records = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()

    def add_wip_entry(self):
        product = self.product_input.text()
        try:
            quantity = int(self.qty_input.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Quantity must be an integer.")
            return
        status = self.status_input.text()
        date = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("INSERT INTO wip VALUES (?, ?, ?, ?)", (product, quantity, status, date))
        conn.commit()
        conn.close()
        self.load_wip_data()

        self.product_input.clear()
        self.qty_input.clear()
        self.status_input.clear()
