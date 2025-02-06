import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess



Logs2s=Tk()
Logs2s.title("Izvelne")
Logs2s.geometry("300x500")
Logs2s.configure(background="#f9f9f9")

def uzlogu1s():
    Logs2s.destroy()
    subprocess.call(['python', 'logs1stud.py'])

def uzlogu3s():
    Logs2s.destroy()
    subprocess.call(['python', 'logs1stud3.py'])

sk=tk.StringVar()

skolotaji=ttk.Combobox(Logs2s, textvariable=sk)
skolotaji.grid(row=1, column=1, pady=10, padx=10)

skolotaji["values"] = ("Skolotajs 1", "Skolotajs 2", "Skolotajs 3")

tk.Button(Logs2s, text="Izvēlēties",font="Arial",bd=5, command=lambda:uzlogu3s()).grid(row=2, column=1, padx=10, pady=10)
tk.Button(Logs2s, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu1s()).grid(row=3, column=1, padx=10, pady=10)


Logs2s.mainloop()