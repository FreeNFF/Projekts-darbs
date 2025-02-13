import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import calendar

Logs5t=Tk()
Logs5t.title("Rediģēšana")
Logs5t.geometry("300x500")
Logs5t.configure(background="#f9f9f9")

ttk.Label(Logs5t, text="Kabinets",font="Arial 15",background='#f9f9f9').grid(row=1, column=1, padx=10, pady=10)
kabinets_entry2 = ttk.Entry(Logs5t, width=10, font="Arial",background='#f9f9f9')
kabinets_entry2.grid(row=2, column=1, padx=20, pady=10)


ttk.Label(Logs5t, text="Konsultācijas laiks",font="Arial 15",background='#f9f9f9').grid(row=3, column=1, padx=10, pady=10)

ttk.Label(Logs5t, text="Sākums",font="Arial 10",background='#f9f9f9').grid(row=4, column=1, padx=5, pady=10)
sakums_entry = ttk.Entry(Logs5t, width=5, font="Arial",background='#f9f9f9')
sakums_entry.grid(row=5, column=1, padx=1, pady=10)

ttk.Label(Logs5t, text="Beigas",font="Arial 10",background='#f9f9f9').grid(row=4, column=2, padx=10, pady=10)
beigas_entry = ttk.Entry(Logs5t, width=5, font="Arial",background='#f9f9f9')
beigas_entry.grid(row=5, column=2, padx=1, pady=10)



tk.Button(Logs5t, text="Labot šo konsultāciju",font="Arial",bd=5,command=lambda:uzlogu3t()).grid(row=8, column=1, padx=20, pady=20)
#tk.Button(Logs5t, text="Labot visas konsultācijas",font="Arial",bd=5,command=lambda:uzlogu3t()).grid(row=9, column=1, padx=20, pady=20)
tk.Button(Logs5t, text="Atgriezties",font="Arial",bd=5,command=lambda:uzlogu4t()).grid(row=10, column=1, padx=20, pady=20)


def uzlogu4t():
    Logs5t.destroy()
    subprocess.call(['python', 'logs4teach.py'])


def uzlogu3t():
    Logs5t.destroy()
    subprocess.call(['python','logs3teach.py'])






Logs5t.mainloop()