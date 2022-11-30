import datetime
from time import ctime
import popup

class Main():
    while(1):
        print("Current date and time")
        now = datetime.datetime.now()
        now = now.strftime("%m-%d-%Y %H:%M:%S")
        popup.Popup.popupmsg(now)
        