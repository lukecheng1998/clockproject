from cProfile import label
import tkinter as tk
from tkinter import ttk
import datetime

LARGE_FONT = ("Helvetica", 156)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

#print("Current date and time")
class Popup():
    def popupmsg(msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg, font=LARGE_FONT)
        label.pack(side="top",fill="x", pady=10)
        popup.attributes("-fullscreen", False)
        popup.after(1000, lambda:popup.destroy())
        popup.mainloop()
    def refresh(self):
        now = datetime.datetime.now()
        now = now.strftime("%m-%d-%Y %H:%M:%S")
        self.config(text=now)
        self.mainloop()
