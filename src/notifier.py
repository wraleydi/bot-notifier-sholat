import os
import sys
import pygame
import tkinter as tk
from tkinter import messagebox

def play_azan():
    script_dir = os.path.dirname(os.path.abspath(__file__))
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

