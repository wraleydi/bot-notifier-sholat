import time
from datetime import datetime
from notifier import show_alert
from hadits import zuhur, ashar, magrib, isya, subuh

def main():
    current_time = datetime.now()

    if current_time.hour == 23 and current_time.minute == 7:
        show_alert("Waktunya Sholat Zuhur!")

    elif current_time.hour == 15 and current_time.minute == 5:
        show_alert("Waktunya Sholat Ashar!")

    elif current_time.hour == 18 and current_time.minute == 0:
        show_alert("Waktunya Sholat Maghrib!")

    elif current_time.hour == 19 and current_time.minute == 5:
        show_alert("Waktunya Sholat Isya!")

    elif current_time.hour == 4 and current_time.minute == 5:
        show_alert("Waktunya Sholat Subuh!")

    time.sleep(60 - current_time.second)

while True:
    main()
