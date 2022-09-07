from cProfile import label
import tkinter as tk
from tkinter import ttk
LARGE_FONT = ("Helvetica", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

print("Current date and time")
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top",fill="x", pady=10)
    popup.mainloop()
