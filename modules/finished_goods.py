from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QHBoxLayout, QMessageBox
import sqlite3

class FinishedGoodsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #121212; color: white; font-size: 14px;")
        layout = QVBoxLayout()

        title = QLabel("Finished Goods")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Input fields
        input_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Product Name")

        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Quantity")

        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("Unit (e.g., boxes, pieces)")

        self.cost_input = QLineEdit()
        self.cost_input.setPlaceholderText("Cost per unit")

        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.quantity_input)
        input_layout.addWidget(self.unit_input)
        input_layout.addWidget(self.cost_input)

        layout.addLayout(input_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Finished Good")
        add_btn.setStyleSheet("background-color: #007BFF; color: white;")
        add_btn.clicked.connect(self.add_finished_good)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_data)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(refresh_btn)
        layout.addLayout(btn_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Product Name", "Quantity", "Unit", "Cost per Unit"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.create_table()
        self.load_data()

    def create_table(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS finished_goods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                quantity REAL,
                unit TEXT,
                cost REAL
            )
        """)
        conn.commit()
        conn.close()

    def add_finished_good(self):
        name = self.name_input.text().strip()
        quantity = self.quantity_input.text().strip()
        unit = self.unit_input.text().strip()
        cost = self.cost_input.text().strip()

        if not name or not quantity or not unit or not cost:
            QMessageBox.warning(self, "Input Error", "Please fill all fields.")
            return

        try:
            quantity = float(quantity)
            cost = float(cost)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Quantity and Cost must be numeric.")
            return

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("INSERT INTO finished_goods (name, quantity, unit, cost) VALUES (?, ?, ?, ?)",
                  (name, quantity, unit, cost))
        conn.commit()
        conn.close()

        self.name_input.clear()
        self.quantity_input.clear()
        self.unit_input.clear()
        self.cost_input.clear()

        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("SELECT * FROM finished_goods")
        rows = c.fetchall()
        conn.close()

        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(rows):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
