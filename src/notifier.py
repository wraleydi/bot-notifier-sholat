import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtCore import Qt, QTimer
import os

app = QApplication(sys.argv)  # Buat satu instance QApplication di awal

class Notifier(QWidget):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("Waktu Sholat")
        self.setGeometry(0, 0, 400, 100)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        label = QLabel(message, self)
        label.setStyleSheet("font-size: 20px; color: white; background-color: black; padding: 20px; border-radius: 10px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        QTimer.singleShot(5000, self.close)  # Notifikasi hilang setelah 5 detik

        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 3)


def show_alert(message):
    print(f"Menampilkan notifikasi: {message}")  # Debugging
    os.system(f'notify-send "Waktu Sholat" "{message}"')


