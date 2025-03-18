import tkinter as tk
import time

def show_notification(prayer_name):
    root = tk.Tk()
    root.title("Notifikasi Sholat")
    label = tk.Label(root, text=f"Waktunya {prayer_name}!", font=("Helvetica", 24))
    label.pack(pady=20)
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack(pady=10)
    root.mainloop()

def schedule_notifications():
    # Daftar waktu sholat (contoh)
    prayer_times = {
        "Subuh": "05:00",
        "Dzuhur": "12:00",
        "Ashar": "15:30",
        "Maghrib": "18:00",
        "Isya": "23:30"
    }

    # Menunggu satu menit sebelum menampilkan notifikasi
    time.sleep(60)

    # Menampilkan notifikasi untuk setiap waktu sholat
    for prayer, prayer_time in prayer_times.items():
        print(f"Menunggu waktu {prayer} pada {prayer_time}...")
        # Tunggu sampai waktu sholat
        current_time = time.strftime("%H:%M")
        while current_time != prayer_time:
            time.sleep(1)  # Tunggu 1 detik
            current_time = time.strftime("%H:%M")
        show_notification(prayer)

# Jalankan fungsi untuk menjadwalkan notifikasi
schedule_notifications()