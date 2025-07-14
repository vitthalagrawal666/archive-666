from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import Qt

class MachinesUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Machine Tasks", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Input Fields
        form_layout = QHBoxLayout()

        self.machine_input = QLineEdit()
        self.machine_input.setPlaceholderText("Machine Name")

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Current Task")

        self.status_combo = QComboBox()
        self.status_combo.addItems(["Idle", "Working", "Maintenance"])

        form_layout.addWidget(self.machine_input)
        form_layout.addWidget(self.task_input)
        form_layout.addWidget(self.status_combo)

        layout.addLayout(form_layout)

        # Button
        self.add_button = QPushButton("Assign Task")
        self.add_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        layout.addWidget(self.add_button)

        # Table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Machine", "Task", "Status"])
        self.table.horizontalHeader().setStyleSheet("background-color: #333; color: white;")
        self.table.setStyleSheet("background-color: #2e2e2e; color: white;")
        layout.addWidget(self.table)

        # Connect logic
        self.add_button.clicked.connect(self.add_task)

    def add_task(self):
        machine = self.machine_input.text()
        task = self.task_input.text()
        status = self.status_combo.currentText()

        if machine and task:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(machine))
            self.table.setItem(row, 1, QTableWidgetItem(task))
            self.table.setItem(row, 2, QTableWidgetItem(status))

            self.machine_input.clear()
            self.task_input.clear()
