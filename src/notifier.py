import os
import sys
import pygame
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import platform
import subprocess

def play_azan():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    current_hour = datetime.now().hour
    if 4 <= current_hour < 5:
        audio_path = os.path.join(script_dir, "azan_subuh.mp3")
    else:
        audio_path = os.path.join(script_dir, "azan.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

def show_alert(message, detailed_message=None):
    try:
        # Coba pakai GUI jika memungkinkan
        if platform.system() == "Linux" and not os.environ.get("DISPLAY"):
            raise RuntimeError("No DISPLAY found for GUI mode")

        root = tk.Tk()
        root.withdraw()

        play_azan()

        if detailed_message:
            messagebox.showinfo("Waktu Sholat", f"{message}\n\n{detailed_message}")
        else:
            messagebox.showinfo("Waktu Sholat", message)

        pygame.mixer.music.stop()
        root.destroy()

    except Exception as e:
        # Fallback ke notifikasi CLI jika gagal GUI
        print(f"[Fallback Notification] {message}")
        play_azan()

        if platform.system() == "Linux":
            try:
                # Kirim notifikasi desktop via notify-send
                subprocess.run([
                    "notify-send", "Waktu Sholat",
                    f"{message}\n{detailed_message or ''}"
                ])
            except Exception as notify_err:
                print("Gagal mengirim notifikasi via notify-send:", notify_err)

        elif platform.system() == "Windows":
            # Kamu bisa tambahkan win10toast atau lib lain untuk Windows
            print("[!] Notifikasi GUI tidak tersedia di Windows fallback mode")

        # Tunggu sampai azan selesai sebelum keluar
        audio_length = pygame.mixer.Sound(audio_path).get_length()
        import time
        time.sleep(audio_length)

        pygame.mixer.music.stop()
