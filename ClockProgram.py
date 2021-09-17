import time
from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text = time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    window.after(1000, update)
window = Tk()

time_label = Label(window, bg = "black", fg = "green", font = ("Arial", 50))
time_label.pack()

day_label = Label(window, font = ("Ink Free", 30))
day_label.pack()

date_label = Label(window, font = ("Ink Free", 30))
date_label.pack()


update()
window.mainloop()