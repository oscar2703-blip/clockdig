from tkinter import*
import random
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title("Clock")
root.geometry("800x150")

def time():
    string = strftime("%H:%M:%S %p %A") #Use capital A for full weekday, and small for abreviated week day name
    lbl.config(text=string)
    lbl.after(1000,time)

lbl = Label(root, font=("ariel", 80, "bold"), background="grey", foreground="white")
lbl.pack(anchor="center")
time()
root.mainloop()