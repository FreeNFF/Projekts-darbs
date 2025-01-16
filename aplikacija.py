import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



#accounts = {"Test" : "Test1", "Test2" : "Password"}




Logs=Tk()# loga objekts
Logs.title("Mācību konsultācijas")
Logs.geometry("300x500")
Logs.configure(background="#f9f9f9")

def login():
    username = username_entry.get()
    password = password_entry.get()

    # print(username, password)

    if username == "john" and password == "parole":
        messagebox.showinfo("Login info", "Welcome John")
    else:
        messagebox.showerror("Piere", "Incorrect username")

ttk.Label(Logs, text="Personas kods",font="Arial 20",background='#f9f9f9').grid(row=2, column=1, padx=30, pady=40)
username_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
username_entry.grid(row=3, column=1, padx=30, pady=10)
ttk.Label(Logs, text="Parole",font="Arial 20",background='#f9f9f9').grid(row=4, column=1, padx=30, pady=40)
password_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
password_entry.grid(row=5, column=1, padx=30, pady=10)

tk.Button(Logs, text="Pieslēgties",font="Arial",bd=5, command=login).grid(row=6, column=1, padx=100, pady=40)

Logs.mainloop()