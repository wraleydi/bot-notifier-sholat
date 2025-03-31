import os
import sys
import pygame
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt, QTimer

def play_azan_and_close(msg_box):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(script_dir, "azan.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    audio_length = pygame.mixer.Sound(audio_path).get_length()

    QTimer.singleShot(int(audio_length * 1000), msg_box.accept)

    msg_box.finished.connect(lambda: pygame.mixer.music.stop())

def show_alert(message, detailed_message=None):
    app = QApplication(sys.argv)

    msg_box = QMessageBox()
    msg_box.setWindowTitle("Waktu Sholat")
    msg_box.setTextFormat(Qt.TextFormat.RichText)
    msg_box.setText(f"<p align='center' style='font-size: 20px;'><b>{message}</b></p>")

    if detailed_message:
        msg_box.setInformativeText(f"<p align='center' style='font-size: 16px;'>{detailed_message}</p>")

    msg_box.setStyleSheet("QLabel{ font-size: 18px; }")
    msg_box.setIcon(QMessageBox.Icon.NoIcon)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Close)

    play_azan_and_close(msg_box)

    msg_box.exec()
