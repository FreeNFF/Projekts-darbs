import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

Logs1t=Tk()# loga objekts
Logs1t.title("Mācību konsultācijas")
Logs1t.geometry("300x500")
Logs1t.configure(background="#f9f9f9")




tk.Button(Logs1t, text="Pieteikt konsultāciju",font="Arial",bd=5, command=lambda:uzlogu2()).grid(row=1, column=1, padx=75, pady=40)
tk.Button(Logs1t, text="Skatīt kalendāru",font="Arial",bd=5, command=lambda:uzlogu3()).grid(row=2, column=1, padx=75, pady=40)
tk.Button(Logs1t, text="Izrakstīties",font="Arial",bd=5, command=lambda:uzlogu1()).grid(row=6, column=1, padx=75, pady=40)

def uzlogu1():
    Logs1t.destroy()
    subprocess.call(['python', '1aplikacija.py'])

def uzlogu2():
    Logs1t.destroy()
    subprocess.call(['python', 'logs2teach.py'])

def uzlogu3():
    Logs1t.destroy()
    subprocess.call(['python', 'logs3teach.py'])

Logs1t.mainloop()