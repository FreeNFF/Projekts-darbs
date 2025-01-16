import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Logs=Tk()# loga objekts
Logs.title("Mācību konsultācijas")
Logs.geometry("300x500")
Logs.configure(background="#f9f9f9")

accounts = {"Test" : "Test1", "Test2" : "Password"}


ttk.Label(Logs, text="Personas kods",font="Arial 20",background='#f9f9f9').grid(row=2, column=1, padx=30, pady=40)
username = ttk.Entry(Logs, font="Arial",background='#f9f9f9').grid(row=3, column=1, padx=30, pady=10)
ttk.Label(Logs, text="Parole",font="Arial 20",background='#f9f9f9').grid(row=4, column=1, padx=30, pady=40)
password = ttk.Entry(Logs, font="Arial",background='#f9f9f9').grid(row=5, column=1, padx=30, pady=10)

tk.Button(Logs, text="Pieslēgties",font="Arial",bd=5).grid(row=6, column=1, padx=100, pady=40, command=lambda:Login())




def Login():
    if (accounts.get(username) == password):
        
    else:
        messagebox.showinfo("Ievadīta nepareiza personas kods vai parole!")
    




Logs.mainloop()