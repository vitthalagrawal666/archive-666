from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QTextEdit
import sqlite3
from datetime import datetime, timedelta

class ReportsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Factory Reports")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()

    def init_ui(self):
        title = QLabel("📊 Factory Reports")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: white;")
        self.layout.addWidget(title)

        self.period_combo = QComboBox()
        self.period_combo.addItems(["Daily", "Weekly", "Monthly", "Annual"])
        self.layout.addWidget(self.period_combo)

        self.report_area = QTextEdit()
        self.report_area.setReadOnly(True)
        self.layout.addWidget(self.report_area)

        generate_btn = QPushButton("Generate Report")
        generate_btn.clicked.connect(self.generate_report)
        self.layout.addWidget(generate_btn)

        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: white; }
            QTextEdit { background-color: #2d2d2d; color: white; border: 1px solid #444; }
            QPushButton { background-color: #007acc; color: white; padding: 6px 12px; }
        """)

    def generate_report(self):
        period = self.period_combo.currentText()
        now = datetime.now()

        if period == "Daily":
            start_date = now - timedelta(days=1)
        elif period == "Weekly":
            start_date = now - timedelta(weeks=1)
        elif period == "Monthly":
            start_date = now.replace(day=1)
        else:  # Annual
            start_date = now.replace(month=1, day=1)

        conn = sqlite3.connect("factory.db")
        c = conn.cursor()

        # Example reports (more can be added similarly)
        c.execute("CREATE TABLE IF NOT EXISTS sales (amount REAL, date TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS purchases (amount REAL, date TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS wages (worker TEXT, amount REAL, date TEXT)")

        c.execute("SELECT SUM(amount) FROM sales WHERE date >= ?", (start_date.strftime("%Y-%m-%d"),))
        total_sales = c.fetchone()[0] or 0

        c.execute("SELECT SUM(amount) FROM purchases WHERE date >= ?", (start_date.strftime("%Y-%m-%d"),))
        total_purchases = c.fetchone()[0] or 0

        c.execute("SELECT SUM(amount) FROM wages WHERE date >= ?", (start_date.strftime("%Y-%m-%d"),))
        total_wages = c.fetchone()[0] or 0

        profit = total_sales - total_purchases - total_wages

        report_text = f"""
📅 Period: {period}
🟢 Total Sales: ₹{total_sales:.2f}
🔵 Total Purchases: ₹{total_purchases:.2f}
🟠 Wages Paid: ₹{total_wages:.2f}
💰 Net Profit: ₹{profit:.2f}
"""

        self.report_area.setText(report_text)
        conn.close()
