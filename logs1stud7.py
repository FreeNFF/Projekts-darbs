import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

Logs7s=Tk()
Logs7s.title("Pieteikuma labošana")
Logs7s.geometry("300x500")
Logs7s.configure(background="#f9f9f9")

def uzlogu5s():
    Logs7s.destroy()
    subprocess.call(['python', 'logs1stud5.py'])




ttk.Label(Logs7s, text="Ko vēlaties darīt mācību konsultācijā:",font="Arial 10",background='#f9f9f9').grid(row=1, column=0, padx=1, pady=10)
info_entry7s = ttk.Entry(Logs7s, width=10, font="Arial",background='#f9f9f9')
info_entry7s.grid(row=2, column=0, padx=20, pady=10)

tk.Button(Logs7s, text="Atgriezties",font="Arial",bd=5,command=lambda:uzlogu5s()).grid(row=3, column=0, padx=20, pady=20)

Logs7s.mainloop()