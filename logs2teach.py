import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


Logs2t=Tk()
Logs2t.title("Mācību konsultācijas")
Logs2t.geometry("300x500")
Logs2t.configure(background="#f9f9f9")


ttk.Label(Logs2t, text="Kabinets",font="Arial 20",background='#f9f9f9').grid(row=1, column=1, padx=30, pady=40)
kabinets_entry = ttk.Entry(Logs2t, font="Arial",background='#f9f9f9')
kabinets_entry.grid(row=2, column=1, padx=30, pady=10)

ttk.Label(Logs2t, text="Konsultācijas laiks",font="Arial 20",background='#f9f9f9').grid(row=3, column=1, padx=30, pady=40)
ttk.Label(Logs2t, text="Sākums",font="Arial 15",background='#f9f9f9').grid(row=4, column=1, padx=30, pady=40)
sakums_entry = ttk.Entry(Logs2t, font="Arial",background='#f9f9f9')
sakums_entry.grid(row=2, column=1, padx=30, pady=10)
ttk.Label(Logs2t, text="Beigas",font="Arial 20",background='#f9f9f9').grid(row=4, column=2, padx=30, pady=40)



tk.Button(Logs2t, text="Pieteikt",font="Arial",bd=5).grid(row=5, column=1, padx=75, pady=40)


Logs2t.mainloop()