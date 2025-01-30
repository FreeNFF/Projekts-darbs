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
 
cal.grid(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())

date= 0
 
# Add Button and Label
Button(Logs3t, text = "Izvēlēties datumu",
       command = grad_date).grid(pady = 20)
 
#date = Label(Logs3t, text = "")
#date.grid(pady = 20)

tk.Button(Logs3t, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu1()).grid(row=2, column=0, padx=20, pady=20)

def uzlogu1():
    Logs3t.destroy()
    subprocess.call(['python', 'logs1teach.py'])

Logs3t.mainloop()