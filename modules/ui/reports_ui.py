from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget, QTextEdit
from PyQt5.QtCore import Qt

class ReportsUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Reports", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Tabs for different report types
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #444; }
            QTabBar::tab { background: #333; padding: 10px; }
            QTabBar::tab:selected { background: #007acc; color: white; }
        """)

        # Create text areas for reports
        self.daily_report = QTextEdit()
        self.weekly_report = QTextEdit()
        self.monthly_report = QTextEdit()
        self.annual_report = QTextEdit()

        # Styling report areas
        for report in [self.daily_report, self.weekly_report, self.monthly_report, self.annual_report]:
            report.setReadOnly(True)
            report.setStyleSheet("background-color: #2e2e2e; color: white;")

        tabs.addTab(self.daily_report, "Daily")
        tabs.addTab(self.weekly_report, "Weekly")
        tabs.addTab(self.monthly_report, "Monthly")
        tabs.addTab(self.annual_report, "Annual")

        layout.addWidget(tabs)

        # Simulated data (Replace with real calculations)
        self.load_dummy_reports()

    def load_dummy_reports(self):
        self.daily_report.setText("Daily Report:\n- Total Sales: ₹10,000\n- Purchases: ₹5,000\n- Wages: ₹2,000\n- Net Profit: ₹3,000")
        self.weekly_report.setText("Weekly Report:\n- Total Sales: ₹70,000\n- Purchases: ₹35,000\n- Wages: ₹14,000\n- Net Profit: ₹21,000")
        self.monthly_report.setText("Monthly Report:\n- Total Sales: ₹3,00,000\n- Purchases: ₹1,50,000\n- Wages: ₹60,000\n- Net Profit: ₹90,000")
        self.annual_report.setText("Annual Report:\n- Total Sales: ₹36,00,000\n- Purchases: ₹18,00,000\n- Wages: ₹7,20,000\n- Net Profit: ₹10,80,000")
