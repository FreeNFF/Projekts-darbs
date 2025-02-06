import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess
import calendar
from datetime import date
from tkcalendar import Calendar

Logs5s=Tk()
Logs5s.title("Kalendārs")
Logs5s.geometry("300x500")
Logs5s.configure(background="#f9f9f9")

sodien = date.today()
sodiend = int(sodien.strftime('%d'))
sodienm = int(sodien.strftime('%m'))
sodieng = int(sodien.strftime('%Y'))


cal = Calendar(Logs5s, selectmode = 'day',
               year = sodieng, month = sodienm,
               day= sodiend)
 
cal.grid(padx=25, pady = 20)

choosen_date= cal.get_date()


def grad_date():
    Logs5s.destroy()
    subprocess.call(['python', 'logs1stud6.py'])



 

Button(Logs5s, text = "Izvēlēties datumu", font="Arial",bd=5, command = grad_date).grid(pady = 20)

tk.Button(Logs5s, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu1s()).grid(row=3, column=0, padx=20, pady=20)

def uzlogu1s():
    Logs5s.destroy()
    subprocess.call(['python', 'logs1stud.py'])




Logs5s.mainloop()