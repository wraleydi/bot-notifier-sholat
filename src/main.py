import time
from datetime import datetime
from notifier import show_alert
from hadits import zuhur, ashar, magrib, isya, subuh

def main():
    current_time = datetime.now()

    if current_time.hour == 12 and current_time.minute == 5:
        formatted_message = f"<p align='center' style='font-size: 16px;'>{zuhur}</p>"
        show_alert("Waktunya Sholat Zuhur!", formatted_message)

    elif current_time.hour == 15 and current_time.minute == 5:
        formatted_message = f"<p align='center' style='font-size: 16px;'>{ashar}</p>"
        show_alert("Waktunya Sholat Ashar!", formatted_message)

    elif current_time.hour == 18 and current_time.minute == 0:
        formatted_message = f"<p align='center' style='font-size: 16px;'>{magrib}</p>"
        show_alert("Waktunya Sholat Maghrib!", formatted_message)

    elif current_time.hour == 19 and current_time.minute == 5:
        formatted_message = f"<p align='center' style='font-size: 16px;'>{isya}</p>"
        show_alert("Waktunya Sholat Isya!", formatted_message)

    elif current_time.hour == 4 and current_time.minute == 5:
        formatted_message = f"<p align='center' style='font-size: 16px;'>{subuh}</p>"
        show_alert("Waktunya Sholat Subuh!", formatted_message)

    time.sleep(60 - current_time.second)

while True:
    main()
