import time
from datetime import datetime
from notifier import show_alert

def main():
    while True:
        current_time = datetime.now()
        
        if current_time.hour == 19 and current_time.minute == 44:
            show_alert("Waktu Sholat Zuhur!")
        
        time.sleep(1)




