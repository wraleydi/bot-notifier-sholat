# ✴️ Sholat Notifier Bot

Script Python sederhana untuk memberikan notifikasi waktu sholat dengan suara adzan dan pop-up message box. Cocok digunakan sebagai bot pengingat otomatis yang aktif setiap perangkat dinyalakan.

---

## 🎧 Fitur

- ✅ Memainkan audio adzan sesuai waktu sholat.
- 🕌 Adzan Subuh menggunakan file khusus (`azan_subuh.mp3`).
- 📦 Notifikasi muncul dalam bentuk message box (GUI).
- ⚙️ Bisa dijalankan otomatis saat boot dengan systemd user service (Linux).

---

## 🔧 Instalasi (Linux)

### 1. Install Dependency Sistem

```
sudo apt update
sudo apt install python3 python3-pip python3-tk
sudo apt install libnotify-bin
```

### 2. Clone Project
```
git clone https://github.com/wraleydi/bot-notifier-sholat.git
```
```
cd bot-notifier-sholat
```
```
pip install -r requirements.txt
```

> _jika sudah coba jalankan manual `python run.py` jika tidak ada error dan tidak muncul apa apa itu karena waktu dari programnya disesuaikan dengan waktu sholat makanya tidak akan tampil apapun_

## ⚙️ Menjadikan sebagai service systemd linux

### 2. Buat File Service
```
sudo nano sholat-notifier.service
```
isi dengan:
```
[Unit]
Description=Sholat Notifier Service
After=network.target

[Service]
ExecStart=/usr/bin/python /home/<your username>/bot-notifier-sholat/run.py
WorkingDirectory=/home/<your username>/bot-notifier-sholat
Restart=always

[Install]
WantedBy=default.target
```

> harap jangan lupa ganti dengan username kalian

```
mkdir -p ~/.config/systemd/user
```
```
cp sholat-notifier.service ~/.config/systemd/user/
```

### 2. Aktifkan dan Jalankan Systemd
```
systemctl --user daemon-reexec
systemctl --user daemon-reload
systemctl --user enable sholat-notifier.service
systemctl --user start sholat-notifier.service
```

> cek status service
```
systemctl --user status sholat-notifier.service
```






