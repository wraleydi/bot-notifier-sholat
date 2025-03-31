import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

def show_alert(message):
    app = QApplication(sys.argv)

    msg_box = QMessageBox()
    msg_box.setWindowTitle("Waktu Sholat")
    msg_box.setText(message)
    msg_box.setIcon(QMessageBox.Icon.Information)  # Bisa diganti Critical, Warning, dll.
    msg_box.setStandardButtons(QMessageBox.StandardButton.Close)

    msg_box.exec()