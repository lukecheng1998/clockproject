import datetime
import time
import popup

class Main():
    while(1):
        print("Current date and time")
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        popup.Popup.popupmsg(now)
        