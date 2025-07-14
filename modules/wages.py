from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
import sqlite3
from datetime import datetime

class WagesScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wages")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()
        self.load_wages()

    def init_ui(self):
        # Title
        title = QLabel("Daily Wages")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(title)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Worker", "Work", "Amount", "Date"])
        self.layout.addWidget(self.table)

        # Inputs
        form_layout = QHBoxLayout()
        self.worker_input = QLineEdit()
        self.worker_input.setPlaceholderText("Worker Name")
        self.work_input = QLineEdit()
        self.work_input.setPlaceholderText("Work Done")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        form_layout.addWidget(self.worker_input)
        form_layout.addWidget(self.work_input)
        form_layout.addWidget(self.amount_input)
        self.layout.addLayout(form_layout)

        # Button
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Entry")
        add_btn.clicked.connect(self.add_wage)
        btn_layout.addWidget(add_btn)
        self.layout.addLayout(btn_layout)

        self.setStyleSheet("QWidget { background-color: #1e1e1e; color: white; } QPushButton { background-color: #007acc; color: white; padding: 5px 10px; }")

    def load_wages(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS wages (
            worker TEXT, work TEXT, amount REAL, date TEXT
        )""")
        c.execute("SELECT * FROM wages")
        wages = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(wages):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()

    def add_wage(self):
        worker = self.worker_input.text()
        work = self.work_input.text()
        amount = self.amount_input.text()
        date = datetime.now().strftime("%Y-%m-%d")

        if not worker or not work or not amount.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Input Error", "Please fill all fields correctly.")
            return

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("INSERT INTO wages VALUES (?, ?, ?, ?)", (worker, work, float(amount), date))
        conn.commit()
        conn.close()
        self.load_wages()

        self.worker_input.clear()
        self.work_input.clear()
        self.amount_input.clear()
