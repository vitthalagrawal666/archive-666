from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox, QComboBox
import sqlite3
from datetime import datetime

class OrdersScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orders")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()
        self.load_orders()

    def init_ui(self):
        # Title
        title = QLabel("Orders")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(title)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Customer", "Product", "Qty", "Status", "Date"])
        self.layout.addWidget(self.table)

        # Inputs
        form_layout = QHBoxLayout()
        self.customer_input = QLineEdit()
        self.customer_input.setPlaceholderText("Customer Name")
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Product")
        self.qty_input = QLineEdit()
        self.qty_input.setPlaceholderText("Quantity")
        self.status_input = QComboBox()
        self.status_input.addItems(["Pending", "In Progress", "Completed"])
        form_layout.addWidget(self.customer_input)
        form_layout.addWidget(self.product_input)
        form_layout.addWidget(self.qty_input)
        form_layout.addWidget(self.status_input)
        self.layout.addLayout(form_layout)

        # Button
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Order")
        add_btn.clicked.connect(self.add_order)
        btn_layout.addWidget(add_btn)
        self.layout.addLayout(btn_layout)

        self.setStyleSheet("QWidget { background-color: #1e1e1e; color: white; } QPushButton { background-color: #007acc; color: white; padding: 5px 10px; }")

    def load_orders(self):
        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS orders (
            customer TEXT, product TEXT, quantity INTEGER,
            status TEXT, date TEXT
        )""")
        c.execute("SELECT * FROM orders")
        orders = c.fetchall()
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(orders):
            self.table.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        conn.close()

    def add_order(self):
        customer = self.customer_input.text()
        product = self.product_input.text()
        quantity = self.qty_input.text()
        status = self.status_input.currentText()
        date = datetime.now().strftime("%Y-%m-%d")

        if not customer or not product or not quantity.isdigit():
            QMessageBox.warning(self, "Input Error", "Please fill all fields correctly.")
            return

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()
        c.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", (customer, product, int(quantity), status, date))
        conn.commit()
        conn.close()
        self.load_orders()

        self.customer_input.clear()
        self.product_input.clear()
        self.qty_input.clear()
