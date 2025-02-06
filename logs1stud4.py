import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

Logs4s=Tk()
Logs4s.title("Pieteikšanās")
Logs4s.geometry("300x500")
Logs4s.configure(background="#f9f9f9")

ttk.Label(Logs4s, text="Informācija par konsultāciju:",font="Arial 15",background='#f9f9f9').grid(row=1, column=0, padx=1, pady=10)
listbox = tk.Listbox(Logs4s, width= 38, height= 10, font="Arial 10",bd=5).grid(row=2, column=0, pady=10, padx=12)

ttk.Label(Logs4s, text="Ko vēlaties darīt mācību konsultācijā:",font="Arial 10",background='#f9f9f9').grid(row=3, column=0, padx=1, pady=10)
info_entry = ttk.Entry(Logs4s, width=10, font="Arial",background='#f9f9f9')
info_entry.grid(row=4, column=0, padx=20, pady=10)





Logs4s.mainloop()