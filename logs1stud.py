import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

Logs1s=Tk()# loga objekts
Logs1s.title("Mācību konsultācijas")
Logs1s.geometry("300x500")
Logs1s.configure(background="#f9f9f9")








tk.Button(Logs1s, text="Pieteikties konsultācijai",font="Arial",bd=5).grid(row=1, column=1, padx=65, pady=40)
tk.Button(Logs1s, text="Skatīt kalendāru",font="Arial",bd=5).grid(row=2, column=1, padx=65, pady=40)
tk.Button(Logs1s, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu1()).grid(row=6, column=1, padx=65, pady=40)

def uzlogu1():
    Logs1s.destroy()
    subprocess.call(['python', 'aplikacija.py'])

Logs1s.mainloop()