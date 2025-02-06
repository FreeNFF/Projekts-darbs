import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import subprocess

# with open('Skoleni.csv','r',encoding='utf-8') as file:
#     csv1 = csv.DictReader(file)
#     data = [row for row in csv1]

# print(data)


#python .\aplikacija.py

Logs=Tk()# loga objekts
Logs.title("Mācību konsultācijas")
Logs.geometry("300x500")
Logs.configure(background="#f9f9f9")

def login():

    lietotaji={}
    username = username_entry.get()
    password = password_entry.get()

    with open('Skoleni.csv',mode='r',newline='', encoding="utf-8") as file:
         csv1 = csv.DictReader(file)
         for row in csv1:
            lietotaji[row['\ufefflietotajs']] = row
            if row['\ufefflietotajs'] == username and row['parole'] == password:
                Logs.destroy()
                subprocess.call(['python', 'logs1stud.py'])
                return

    with open('Skolotaji.csv',mode='r',newline='', encoding="utf-8") as file:
        csv1 = csv.DictReader(file)
        for row in csv1:
            lietotaji[row['\ufefflietotajs']] = row
            if row['\ufefflietotajs'] == username and row['parole'] == password:
                Logs.destroy()
                subprocess.call(['python', 'logs1teach.py'])
                return
    messagebox.showerror("Kļūda", "Nepareizs lietotāja vārds vai parole!")


ttk.Label(Logs, text="Lietotājvārds",font="Arial 20",background='#f9f9f9').grid(row=2, column=1, padx=30, pady=40)
username_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
username_entry.grid(row=3, column=1, padx=30, pady=10)
ttk.Label(Logs, text="Parole",font="Arial 20",background='#f9f9f9').grid(row=4, column=1, padx=30, pady=40)
password_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
password_entry.grid(row=5, column=1, padx=30, pady=10)




tk.Button(Logs, text="Pieslēgties",font="Arial",bd=5, command=login).grid(row=6, column=1, padx=100, pady=40)

Logs.mainloop()