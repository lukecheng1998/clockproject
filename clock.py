from tkinter import *
from tkinter.ttk import *
import datetime
import platform
try:
    import winsound #windows
except:
    import os #other
window = Tk()
window.title("Clock")
window.geometry('500x250')
tabsControl = Notebook(window)
clockTab = Frame(tabsControl)
tabsControl.add(clockTab, text="Clock")
tabsControl.pack(expand = 1, fill = "both")
timeLabel = Label(clockTab, font = 'Helvetica 40 bold', foreground = 'white')
timeLabel.pack(anchor='center')
dateLabel = Label(clockTab, font = 'Helvetica 40 bold', foreground = 'white')
dateLabel.pack(anchor='s')

def clock():
    dateTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S/%p")
    date, time1 = dateTime.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    if (int(hour) > 12 and int(hour) < 24):#calculate time
        time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
        time = time2 + ' ' + time3
    timeLabel.config(text = time)
    dateLabel.config(text = date)
    timeLabel.after(1000, clock)
clock()
window.mainloop()