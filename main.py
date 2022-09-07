import datetime
import time
import popup

print("Current date and time")
class Main():
    while(1):
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        popup.popupmsg(now)
        time.sleep(1)