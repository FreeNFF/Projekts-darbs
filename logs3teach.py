import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from tkcalendar import Calendar

Logs3t=Tk()
Logs3t.title("Kalendārs")
Logs3t.geometry("300x500")
Logs3t.configure(background="#f9f9f9")

cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
cal.pack(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(root, text = "")
date.pack(pady = 20)




Logs3t.mainloop()