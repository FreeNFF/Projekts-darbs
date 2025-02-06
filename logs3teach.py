import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import calendar
from datetime import date
from tkcalendar import Calendar #+ terminālī pip install tkcalendar

Logs3t=Tk()
Logs3t.title("Kalendārs")
Logs3t.geometry("300x500")
Logs3t.configure(background="#f9f9f9")

sodien = date.today()
sodiend = int(sodien.strftime('%d'))
sodienm = int(sodien.strftime('%m'))
sodieng = int(sodien.strftime('%Y'))


cal = Calendar(Logs3t, selectmode = 'day',
               year = sodieng, month = sodienm,
               day= sodiend)
 
cal.grid(padx=25, pady = 20)

choosen_date= cal.get_date()


def grad_date():
    Logs3t.destroy()
    subprocess.call(['python', 'logs4teach.py'])



 
# Add Button and Label
Button(Logs3t, text = "Izvēlēties datumu", font="Arial",bd=5, command = grad_date).grid(pady = 20)

tk.Button(Logs3t, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu1()).grid(row=3, column=0, padx=20, pady=20)

def uzlogu1():
    Logs3t.destroy()
    subprocess.call(['python', 'logs1teach.py'])

Logs3t.mainloop()