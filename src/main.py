import time
from datetime import datetime
from notifier import show_alert

def main():
    current_time = datetime.now()

    if current_time.hour == 22 and current_time.minute == 42:
        show_alert("Waktunya Sholat Zuhur!")

    elif current_time.hour == 15 and current_time.minute == 5:
        show_alert("Waktunya Sholat Ashar!")

    elif current_time.hour == 18 and current_time.minute == 0:
        show_alert("Waktunya Sholat Maghrib!")

    elif current_time.hour == 19 and current_time.minute == 5:
        show_alert("Waktunya Sholat Isya!")

    elif current_time.hour == 4 and current_time.minute == 30:
        show_alert("Waktunya Sholat Subuh!")

    time.sleep(60 - current_time.second)

while True:
    main()
