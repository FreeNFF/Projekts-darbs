import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


Logs1s=Tk()# loga objekts
Logs1s.title("Mācību konsultācijas")
Logs1s.geometry("300x500")
Logs1s.configure(background="#f9f9f9")

tk.Button(Logs1s, text="Pieteikties konsultācijai",font="Arial",bd=5).grid(row=1, column=1, padx=65, pady=40)
tk.Button(Logs1s, text="Skatīt kalendāru",font="Arial",bd=5).grid(row=2, column=1, padx=65, pady=40)
tk.Button(Logs1s, text="Atgriezties",font="Arial",bd=5).grid(row=6, column=1, padx=65, pady=40)

Logs1s.mainloop()