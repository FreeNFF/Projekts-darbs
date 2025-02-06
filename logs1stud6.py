import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

Logs6s=Tk()
Logs6s.title("Izvelne")
Logs6s.geometry("300x500")
Logs6s.configure(background="#f9f9f9")

ttk.Label(Logs6s, text="Informācija par pieteikumu:",font="Arial 15",background='#f9f9f9').grid(row=1, column=0, padx=1, pady=10)
listbox = tk.Listbox(Logs6s, width= 38, height= 10, font="Arial 10",bd=5).grid(row=2, column=0, pady=10, padx=12)

tk.Button(Logs6s, text="Atgriezties",font="Arial",bd=5).grid(row=3, column=0, padx=20, pady=20)
tk.Button(Logs6s, text="Atgriezties",font="Arial",bd=5).grid(row=3, column=1, padx=20, pady=20)

Logs6s.mainloop()