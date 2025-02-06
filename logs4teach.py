import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import calendar
from logs3teach import choosen_date

Logs4t=Tk()
Logs4t.title("Konsultācija")
Logs4t.geometry("300x500")
Logs4t.configure(background="#f9f9f9")

ttk.Label(Logs4t, text="Pieteikumi:",font="Arial 15",background='#f9f9f9').grid(row=1, column=0, padx=1, pady=10)
listbox = tk.Listbox(Logs4t, width= 38, height= 10, font="Arial 10",bd=5).grid(row=2, column=0, pady=10, padx=12)

tk.Button(Logs4t, text="Dzēst",font="Arial",bd=5).grid(row=4, column=0, padx=1, pady=10)
tk.Button(Logs4t, text="Labot",font="Arial",bd=5, command=lambda:uzlogu5()).grid(row=3, column=0, padx=1, pady=10)
tk.Button(Logs4t, text="Dzēst visas",font="Arial",bd=5).grid(row=5, column=0, padx=1, pady=10)

tk.Button(Logs4t, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu4()).grid(row=6, column=0, padx=10, pady=10)

def uzlogu4():
    Logs4t.destroy()
    subprocess.call(['python', 'logs3teach.py'])

def uzlogu5():
    Logs4t.destroy()
    subprocess.call(['python', 'logs5teach.py'])
