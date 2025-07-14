import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

class ExportUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout(self)

        title = QLabel("Export & Print Reports", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        export_btn = QPushButton("Export Sample Report to Excel")
        export_btn.setStyleSheet(self.button_style())
        export_btn.clicked.connect(self.export_to_excel)
        layout.addWidget(export_btn)

        print_btn = QPushButton("Print Preview")
        print_btn.setStyleSheet(self.button_style())
        print_btn.clicked.connect(self.print_preview)
        layout.addWidget(print_btn)

    def button_style(self):
        return """
            QPushButton {
                background-color: #0078d7;
                color: white;
                padding: 10px;
                font-size: 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #005999;
            }
        """

    def export_to_excel(self):
        data = {
            "Date": ["2025-06-25", "2025-06-24"],
            "Product": ["Red Gulal", "Hawan Samagri"],
            "Quantity (kg)": [500, 300],
            "Status": ["Completed", "In Progress"]
        }
        df = pd.DataFrame(data)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            try:
                df.to_excel(file_path, index=False)
                QMessageBox.information(self, "Success", "Report exported successfully.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Export failed:\n{str(e)}")

    def print_preview(self):
        QMessageBox.information(self, "Print Preview", "This feature will open a print preview window.\n(Coming soon)")
