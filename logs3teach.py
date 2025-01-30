import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import calendar
from tkcalendar import Calendar #+ terminālī pip install tkcalendar

Logs3t=Tk()
Logs3t.title("Kalendārs")
Logs3t.geometry("300x500")
Logs3t.configure(background="#f9f9f9")

cal = Calendar(Logs3t, selectmode = 'day',
               year = 2025, month = 1,
               day = 22)
 
cal.pack(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(Logs3t, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(Logs3t, text = "")
date.pack(pady = 20)




Logs3t.mainloop()