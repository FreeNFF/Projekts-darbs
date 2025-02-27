import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import subprocess#pip install tkcalendar
from PIL import Image, ImageTk

def start_move(event):
    window = event.widget.winfo_toplevel()
    window.x = event.x_root - window.winfo_x()
    window.y = event.y_root - window.winfo_y()

def move_window(event):
    window = event.widget.winfo_toplevel()
    x = event.x_root - window.x
    y = event.y_root - window.y
    window.geometry(f"+{x}+{y}")

Logs=tk.Tk()# loga objekts
Logs.title("Mācību konsultācijas")
Logs.geometry("300x500")
Logs.configure(background="#f9f9f9")
Logs.overrideredirect(True)
Logs.wm_attributes("-topmost", True)
Logs.wm_attributes("-toolwindow", False)
Logs.wm_withdraw()  
Logs.after(10, Logs.wm_deiconify)




title_bar = tk.Frame(Logs, bg="#98c41c", relief="raised", bd=2)
title_bar.pack(side="top", fill="x")

title_label = tk.Label(title_bar, text="Mācību konsultācijas", font=("Roboto",12,"bold"), bg="#98c41c", fg="#f9f9f9")
title_label.pack(side="left", padx=10)

close_button = tk.Button(title_bar, text="X", bg="red", fg="#f9f9f9", command=Logs.destroy)
close_button.pack(side="right", padx=5)

title_bar.bind("<Button-1>", start_move)  
title_bar.bind("<B1-Motion>", move_window)  

content_frame = tk.Frame(Logs, bg="#f9f9f9")
content_frame.pack(fill="both", expand=True)

def login():

    lietotaji={}
    username = username_entry.get()
    password = password_entry.get()

    with open('Skoleni.csv',mode='r',newline='', encoding="utf-8") as file:
         csv1 = csv.DictReader(file)
         for row in csv1:
            lietotaji[row['\ufefflietotajs']] = row
            if row['\ufefflietotajs'] == username and row['parole'] == password:
                print(username)
                Logs.destroy()
                subprocess.call(['python', 'aplikacija2.py'])
                return

    with open('Skolotaji.csv',mode='r',newline='', encoding="utf-8") as file:
        csv1 = csv.DictReader(file)
        for row in csv1:
            lietotaji[row['\ufefflietotajs']] = row
            if row['\ufefflietotajs'] == username and row['parole'] == password:
                print(username)
                Logs.destroy()
                subprocess.call(['python', 'aplikacija3.py'])
                return
    messagebox.showerror("Kļūda", "Nepareizs lietotāja vārds vai parole!")
    return username

ttk.Label(Logs, text="Lietotājvārds",font="Arial 20",background='#f9f9f9').pack(pady=14)
username_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
username_entry.pack(pady=14)
ttk.Label(Logs, text="Parole",font="Arial 20",background='#f9f9f9').pack(pady=14)
password_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
password_entry = ttk.Entry(Logs, show="*")#Ievadot paroli rāda "*" simbolu vietā
password_entry.pack(pady=14)

tk.Button(Logs, text="Pieslēgties",font="Arial",bd=5, command=login,fg="green").pack(pady=14)

foto_frame=tk.Frame(Logs, background='#f9f9f9')
foto_frame.pack(pady=14)
foto_image=Image.open("Kekavas vidusskola-870x1110_11.png")
resized_foto=foto_image.resize((100,120))
foto = ImageTk.PhotoImage(resized_foto)
foto_label=ttk.Label(foto_frame,image=foto, background='#f9f9f9')
foto_label.pack(pady=14)

Logs.mainloop()

# with open('Skoleni.csv','r',encoding='utf-8') as file:
#     csv1 = csv.DictReader(file)
#     data = [row for row in csv1]

# print(data)


#python .\aplikacija.py

#-------------------------------------
#1. Variants
#
# Atseviscā failā vert.py
# VALUE = 222
# Vajadzigajos failos:
# from constants import VALUE
#
# 2. Variants
# Main failā: 
# import os
# os.environ["MY_CONSTANT"] = "42"  # Set once in a main script
# 
# Citos failos: 
# import os
# MY_CONSTANT = int(os.getenv("MY_CONSTANT", 42))  # Ensure it stays the same
#





# Logs=Tk()# loga objekts
# Logs.title("Mācību konsultācijas")
# Logs.geometry("300x500")
# Logs.configure(background="#f9f9f9")

# global username

# def login():

#     lietotaji={}
#     username = username_entry.get()
#     password = password_entry.get()

#     with open('Skoleni.csv',mode='r',newline='', encoding="utf-8") as file:
#          csv1 = csv.DictReader(file)
#          for row in csv1:
#             lietotaji[row['\ufefflietotajs']] = row
#             if row['\ufefflietotajs'] == username and row['parole'] == password:
#                 print(username)
#                 Logs.destroy()
#                 subprocess.call(['python', 'aplikacija2.py'])
#                 return

#     with open('Skolotaji.csv',mode='r',newline='', encoding="utf-8") as file:
#         csv1 = csv.DictReader(file)
#         for row in csv1:
#             lietotaji[row['\ufefflietotajs']] = row
#             if row['\ufefflietotajs'] == username and row['parole'] == password:
#                 print(username)
#                 Logs.destroy()
#                 subprocess.call(['python', 'aplikacija3.py'])
#                 return
#     messagebox.showerror("Kļūda", "Nepareizs lietotāja vārds vai parole!")
#     return username




# ttk.Label(Logs, text="Lietotājvārds",font="Arial 20",background='#f9f9f9').grid(row=2, column=1, padx=30, pady=14)
# username_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
# username_entry.grid(row=3, column=1, padx=30, pady=14)
# ttk.Label(Logs, text="Parole",font="Arial 20",background='#f9f9f9').grid(row=4, column=1, padx=30, pady=14)
# password_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
# password_entry = ttk.Entry(Logs, show="*")#Ievadot paroli rāda "*" simbolu vietā
# password_entry.grid(row=5, column=1, padx=30, pady=14)

# tk.Button(Logs, text="Pieslēgties",font="Arial",bd=5, command=login,fg="green").grid(row=6, column=1, padx=100, pady=14)

# foto_frame=tk.Frame(Logs, background='#f9f9f9')
# foto_frame.grid(row=7,column=1,padx=10,pady=14)
# foto_image=Image.open("Kekavas vidusskola-870x1110_11.png")
# resized_foto=foto_image.resize((100,120))
# foto = ImageTk.PhotoImage(resized_foto)
# foto_label=ttk.Label(foto_frame,image=foto, background='#f9f9f9')
# foto_label.grid(row=7,column=1,padx=10,pady=14)

# Logs.mainloop()











