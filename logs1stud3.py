import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import calendar
from datetime import date
from tkcalendar import Calendar

Logs3s=Tk()
Logs3s.title("Kalendārs")
Logs3s.geometry("300x500")
Logs3s.configure(background="#f9f9f9")

sodien = date.today()
sodiend = int(sodien.strftime('%d'))
sodienm = int(sodien.strftime('%m'))
sodieng = int(sodien.strftime('%Y'))


cal = Calendar(Logs3s, selectmode = 'day',
               year = sodieng, month = sodienm,
               day= sodiend)
 


cal.grid(padx=25, pady = 20)


choosen_date= cal.get_date()


def grad_date():
    Logs3s.destroy()
    subprocess.call(['python', 'logs1stud4.py'])



 

Button(Logs3s, text = "Izvēlēties datumu", font="Arial",bd=5, command = grad_date).grid(pady = 20)

tk.Button(Logs3s, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu2s()).grid(row=3, column=0, padx=20, pady=20)

def uzlogu2s():
    Logs3s.destroy()
    subprocess.call(['python', 'logs1stud2.py'])




Logs3s.mainloop()