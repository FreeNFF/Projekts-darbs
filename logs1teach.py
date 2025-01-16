import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

Logs1t=Tk()# loga objekts
Logs1t.title("Mācību konsultācijas")
Logs1t.geometry("300x500")
Logs1t.configure(background="#f9f9f9")




tk.Button(Logs1t, text="Pieteikt konsultāciju",font="Arial",bd=5).grid(row=1, column=1, padx=75, pady=40)
tk.Button(Logs1t, text="Skatīt kalendāru",font="Arial",bd=5).grid(row=2, column=1, padx=75, pady=40)
tk.Button(Logs1t, text="Atgriezties",font="Arial",bd=5).grid(row=6, column=1, padx=75, pady=40)

Logs1t.mainloop()