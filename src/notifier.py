import os
import pygame
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def play_azan():
    # Tentukan path ke file audio
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Dapatkan jam saat ini
    current_hour = datetime.now().hour

    # Tentukan file azan yang akan diputar
    if current_hour >= 4 and current_hour < 5:
        audio_path = os.path.join(script_dir, "azan_subuh.mp3")
    else:
        audio_path = os.path.join(script_dir, "azan.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play() 

def show_alert(message, detailed_message=None):
    root = tk.Tk()
    root.withdraw()

    play_azan()

    if detailed_message:
        messagebox.showinfo("Waktu Sholat", f"{message}\n\n{detailed_message}")
    else:
        messagebox.showinfo("Waktu Sholat", message)

    pygame.mixer.music.stop()
    root.destroy() 

