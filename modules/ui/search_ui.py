from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt

class SearchUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout(self)

        title = QLabel("Search Records", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Search input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter keyword to search...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #2e2e2e;
                color: white;
                padding: 8px;
                border: 1px solid #555;
                font-size: 14px;
            }
        """)
        self.search_input.returnPressed.connect(self.perform_search)
        layout.addWidget(self.search_input)

        # Search result display
        self.search_results = QTextEdit()
        self.search_results.setReadOnly(True)
        self.search_results.setStyleSheet("background-color: #2e2e2e; color: white; font-size: 14px;")
        layout.addWidget(self.search_results)

    def perform_search(self):
        keyword = self.search_input.text().strip().lower()
        if not keyword:
            self.search_results.setText("Please enter a keyword to search.")
            return

        # Dummy records (to simulate)
        records = [
            "Order #123: 500kg Red Gulal - Pending",
            "Raw Material: Arrowroot Powder - 100kg in stock",
            "Wage Entry: Ramesh - ₹500 - 24th June",
            "Finished Product: Hawan Samagri - 20kg",
            "Machine Task: Mixing Machine - Red Color Batch"
        ]

        # Filtered result
        filtered = [rec for rec in records if keyword in rec.lower()]
        if filtered:
            self.search_results.setText("\n".join(filtered))
        else:
            self.search_results.setText("No results found.")
