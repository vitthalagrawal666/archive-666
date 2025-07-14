import os
import shutil
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

class BackupRestoreUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout(self)

        title = QLabel("Backup & Restore", alignment=Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        backup_btn = QPushButton("Backup Database")
        backup_btn.setStyleSheet(self.button_style())
        backup_btn.clicked.connect(self.backup_db)
        layout.addWidget(backup_btn)

        restore_btn = QPushButton("Restore Database")
        restore_btn.setStyleSheet(self.button_style())
        restore_btn.clicked.connect(self.restore_db)
        layout.addWidget(restore_btn)

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

    def backup_db(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Backup File", "", "SQLite DB (*.db)")
        if file_path:
            try:
                shutil.copyfile("data/database.db", file_path)
                QMessageBox.information(self, "Backup Complete", "Database backup successful.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Backup failed:\n{str(e)}")

    def restore_db(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Backup File", "", "SQLite DB (*.db)")
        if file_path:
            try:
                shutil.copyfile(file_path, "data/database.db")
                QMessageBox.information(self, "Restore Complete", "Database restored successfully.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Restore failed:\n{str(e)}")
