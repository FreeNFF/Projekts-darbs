import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess



Logs2t=Tk()
Logs2t.title("Mācību konsultācijas")
Logs2t.geometry("300x500")
Logs2t.configure(background="#f9f9f9")

global kabinets_entry
global sakums_entry
global beigas_entry
global diena_entry


global kabinets
global kons_sakums
global beigas_kons
global diena



ttk.Label(Logs2t, text="Kabinets",font="Arial 15",background='#f9f9f9').grid(row=1, column=1, padx=10, pady=10)
kabinets_entry = ttk.Entry(Logs2t, width=10, font="Arial",background='#f9f9f9')
kabinets_entry.grid(row=2, column=1, padx=20, pady=10)

kabinets = kabinets_entry.get()

ttk.Label(Logs2t, text="Konsultācijas laiks",font="Arial 15",background='#f9f9f9').grid(row=3, column=1, padx=10, pady=10)

ttk.Label(Logs2t, text="Sākums",font="Arial 10",background='#f9f9f9').grid(row=4, column=1, padx=5, pady=10)
sakums_entry = ttk.Entry(Logs2t, width=5, font="Arial",background='#f9f9f9')
sakums_entry.grid(row=5, column=1, padx=5, pady=10)

kons_sakums= sakums_entry.get()

ttk.Label(Logs2t, text="Beigas",font="Arial 10",background='#f9f9f9').grid(row=4, column=2, padx=10, pady=10)
beigas_entry = ttk.Entry(Logs2t, width=5, font="Arial",background='#f9f9f9')
beigas_entry.grid(row=5, column=2, padx=10, pady=10)

beigas_kons = beigas_entry.get()

ttk.Label(Logs2t, text="Diena (angliski)",font="Arial 10",background='#f9f9f9').grid(row=6, column=1, padx=5, pady=10)
diena_entry = ttk.Entry(Logs2t, width=5, font="Arial",background='#f9f9f9')
diena_entry.grid(row=7, column=1, padx=10, pady=10)


tk.Button(Logs2t, text="Pieteikt",font="Arial",bd=5, command=lambda:uzlogu1()).grid(row=8, column=1, padx=20, pady=20)
tk.Button(Logs2t, text="Atgriezties",font="Arial",bd=5, command=lambda:uzlogu1()).grid(row=9, column=1, padx=20, pady=20)

def uzlogu1():
    Logs2t.destroy()
    subprocess.call(['python', 'logs1teach.py'])



Logs2t.mainloop()