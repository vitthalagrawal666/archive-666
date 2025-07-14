from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
import sqlite3
from datetime import datetime

class MachinesScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Machines")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()
        self.load_machines()

    def init_ui(self):
        # Title
        title = QLabel("Machine Tasks")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(title)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Machine Name", "Assigned Task", "Status", "Date"])
        self.layout.addWidget(self.table)

        # Inputs
        form_layout = QHBoxLayout()
        self.machine_input = QLineEdit()
        self.machine_input.setPlaceholderText("Machine Name")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Assigned Task")
        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Status")
        form_layout.addWidget(self.machine_input)
        form_layout.addWidget(self.task_input)
        form_layout.addWidget(self.status_input)
        self.layout.addLayout(form_layout)

        # Button
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Assign Task")
        add_btn.clicked.connect(self.add_machine_task)
        btn_layout.addWidget(add_btn)
        self.layout.addLayout(btn_layout)

        self.setStyleSheet("QWidget { background-color: #1e1e1e; color: white; } QPushButton { background-color: #007acc; color: white; padding: 5px 10px; }")

    def load_machines(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS machines (
            machine_name TEXT, task TEXT, status TEXT, date TEXT
        )""")
        c.execute("SELECT * FROM machines")
        records = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()

    def add_machine_task(self):
        machine = self.machine_input.text()
        task = self.task_input.text()
        status = self.status_input.text()
        date = datetime.now().strftime("%Y-%m-%d")

        if not machine or not task or not status:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
            return

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("INSERT INTO machines VALUES (?, ?, ?, ?)", (machine, task, status, date))
        conn.commit()
        conn.close()
        self.load_machines()

        self.machine_input.clear()
        self.task_input.clear()
        self.status_input.clear()
