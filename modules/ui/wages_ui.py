from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from datetime import datetime

class WagesUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Daily Wage & Labour Records", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Input Section
        form_layout = QHBoxLayout()

        self.worker_input = QLineEdit()
        self.worker_input.setPlaceholderText("Worker Name")

        self.work_input = QLineEdit()
        self.work_input.setPlaceholderText("Work Done")

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Wage Amount")

        form_layout.addWidget(self.worker_input)
        form_layout.addWidget(self.work_input)
        form_layout.addWidget(self.amount_input)

        layout.addLayout(form_layout)

        # Button
        self.add_button = QPushButton("Add Wage Record")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        layout.addWidget(self.add_button)

        # Table
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Date", "Worker", "Work Done", "Amount"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect logic
        self.add_button.clicked.connect(self.add_record)

    def add_record(self):
        worker = self.worker_input.text()
        work = self.work_input.text()
        amount = self.amount_input.text()
        date_str = datetime.now().strftime("%Y-%m-%d")

        if worker and work and amount:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(date_str))
            self.table.setItem(row, 1, QTableWidgetItem(worker))
            self.table.setItem(row, 2, QTableWidgetItem(work))
            self.table.setItem(row, 3, QTableWidgetItem(amount))

            self.worker_input.clear()
            self.work_input.clear()
            self.amount_input.clear()
