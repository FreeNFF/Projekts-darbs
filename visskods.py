# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# import csv
# import subprocess#pip install tkcalendar
# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# import subprocess
# import calendar
# from tkcalendar import Calendar
# from datetime import date
# import datetime
# import json

# root=Tk()# loga objekts
# root.title("Mācību konsultācijas")
# root.geometry("300x500")
# root.configure(background="#f9f9f9")

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
#                 root.destroy()
#                 if __name__ == "__main__":
#                     root = tk.Tk()
#                     app = CalendarAppS(root)
#                     root.mainloop()
#                 return

#     with open('Skolotaji.csv',mode='r',newline='', encoding="utf-8") as file:
#         csv1 = csv.DictReader(file)
#         for row in csv1:
#             lietotaji[row['\ufefflietotajs']] = row
#             if row['\ufefflietotajs'] == username and row['parole'] == password:
#                 print(username)
#                 root.destroy()
#                 if __name__ == "__main__":
#                     root = tk.Tk()
#                     app = CalendarAppT(root)
#                     root1.mainloop()
#                 return
#     messagebox.showerror("Kļūda", "Nepareizs lietotāja vārds vai parole!")
#     return username




# ttk.Label(root, text="Lietotājvārds",font="Arial 20",background='#f9f9f9').grid(row=2, column=1, padx=30, pady=40)
# username_entry = ttk.Entry(root, font="Arial",background='#f9f9f9')
# username_entry.grid(row=3, column=1, padx=30, pady=10)
# ttk.Label(root, text="Parole",font="Arial 20",background='#f9f9f9').grid(row=4, column=1, padx=30, pady=40)
# password_entry = ttk.Entry(root, font="Arial",background='#f9f9f9')
# password_entry = ttk.Entry(root, show="*")#Ievadot paroli rāda "*" simbolu vietā
# password_entry.grid(row=5, column=1, padx=30, pady=10)

# tk.Button(root, text="Pieslēgties",font="Arial",bd=5, command=login).grid(row=6, column=1, padx=100, pady=40)

# class CalendarAppS:#izveido klasi
#     def __init__(self, root):#izveido jaunu logu
#         self.root = root#pārdēvē logu
#         self.root.title("Konsultāciju kalendārs")#loga nosaukums
#         root.geometry("300x500")#loga izmēri
#         self.data_file = "calendar_data.json"#atver jau ievadītos vai izveido jaunu failu kur saglabāsies dati
#         self.data = self.load_data()#pievieno funkciju., kurā ielādē jau ievadītos datus
        
#         self.create_main_page()#paša loga izveides funkcija
    
#     def create_main_page(self):#izveido kalendāru un pogas
#         frame = ttk.Frame(self.root)#izveido rāmi
#         frame.pack(pady=20, padx=20)#novieto rāmi
        
#         self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")#kalendāru ievieto rāmi(izveido kalendāru)
#         self.calendar.pack()
        
#         self.highlight_dates()

#         view_button = ttk.Button(frame, text="Apskatīt konsultāciju", command=self.view_details)#Poga info apskatīšanai
#         view_button.pack(pady=20)

#         izrakstisanas = ttk.Button(root, text="Izrakstīties", command=self.uzlogu1)
#         izrakstisanas.pack(pady=20)#Izrakstīšanās poga
        
#     def uzlogu1(self):#Funkcija izrakstīšanās pogai
#         root.destroy()#Aizver logu
#         subprocess.call(['python', 'aplikacija.py'])#Atver pierakstīšanās logu
    
#     def view_details(self):
#         selected_date = self.calendar.get_date()
#         info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")
        
#         details_window = tk.Toplevel(self.root)
#         details_window.geometry("300x500")
#         details_window.title(f"Informācija {selected_date}")

#         self.details_window = details_window

#         ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
#         ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
#         ttk.Button(details_window, text="Pieteikties", command=self.pieteikties).pack(pady=10)
#         ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)
        
        
#     def pieteikties(self):
#     # Aizver "Apskatīt konsultāciju" logu
#         if hasattr(self, 'details_window') and self.details_window:
#             self.details_window.destroy()  # Aizver "Apskatīt konsultāciju" logu
    
#         selected_date = self.calendar.get_date()
#         pieteikties_logs  = tk.Toplevel(self.root)
#         pieteikties_logs.geometry("300x500")
#         pieteikties_logs.title(f"Pieteikšanās {selected_date}")

#     # Ievades lauki vārdiem, uzvārdiem un konsultācijas tēmai
#         ttk.Label(pieteikties_logs, text="Vārds:").pack(pady=5)
#         vards_entry = ttk.Entry(pieteikties_logs)
#         vards_entry.pack(pady=5)

#         ttk.Label(pieteikties_logs, text="Uzvārds:").pack(pady=5)
#         uzvards_entry = ttk.Entry(pieteikties_logs)
#         uzvards_entry.pack(pady=5)

#         ttk.Label(pieteikties_logs, text="Konsultācijas tēma:").pack(pady=5)
#         temats_entry = ttk.Entry(pieteikties_logs)
#         temats_entry.pack(pady=5)

#     # Funkcija, lai saglabātu pieteikšanos
#         def save_pieteikums():
#             #konsultacija =
#             #text_entry1 = os.getenv("text_entry1", text_entry)
#             vards = vards_entry.get()
#             uzvards = uzvards_entry.get()
#             temats = temats_entry.get()

#             if not vards or not uzvards or not temats:
#                 messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus!")
#                 return

#         # Saglabā pieteikšanās informāciju JSON failā
#             pieteikums = {
#                 "Konsultacija":"",
#                 "vards": vards,
#                 "uzvards": uzvards,
#                 "temats": temats
#             }

#         # Nodrošina, ka self.data[selected_date] ir saraksts, ja tas vēl nav
#             if selected_date not in self.data or not isinstance(self.data[selected_date], list):
#                 self.data[selected_date] = []  # Ja nav saraksta, izveido tukšu sarakstu

#             self.data[selected_date].append(pieteikums)  # Pievieno pieteikumu sarakstam

#         # Saglabā datus
#             self.save_data()

#             messagebox.showinfo("Pieteikšanās apstiprinājums", f"Pieteikšanās veiksmīgi saglabāta datumam {selected_date}!")
#             pieteikties_logs.destroy()

#     # Poga, lai saglabātu pieteikšanos
#         ttk.Button(pieteikties_logs, text="Pieteikties", command=save_pieteikums).pack(pady=10)

#     # Poga, lai aizvērtu logu
#         ttk.Button(pieteikties_logs, text="Aizvērt", command=pieteikties_logs.destroy).pack(pady=5)





#     def highlight_dates(self, calendar_widget=None):
#         calendar_widget = calendar_widget or self.calendar  # Clear previous highlights
#         calendar_widget.calevent_remove('all')
#         # Configure event tag for highlighting
#         calendar_widget.tag_config("reminder", background="yellow", foreground="black")

#         for date_str in self.data.keys():
#             try:
#                 # Convert string date to datetime object
#                 date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
#                 # Ensure date is correctly added to the calendar
#                 calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")
#             except ValueError:
#                 continue  # Skip invalid date formats

#         calendar_widget.update_idletasks()  # Refresh UI to show highlights
    

#     def save_data(self):
#         with open(self.data_file, "w") as file:
#             json.dump(self.data, file)
    
#     def load_data(self):
#         try:
#             with open(self.data_file, "r") as file:
#                 return json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return {}

# class CalendarAppT:#izveido klasi
#     def __init__(self, root1):#izveido jaunu logu
#         self.root1 = root1#pārdēvē logu
#         self.root1.title("Konsultāciju kalendārs")#loga nosaukums
#         root1.geometry("300x500")#loga izmēri
#         self.data_file = "calendar_data.json"#atver jau ievadītos vai izveido jaunu failu kur saglabāsies dati
#         self.data = self.load_data()#pievieno funkciju., kurā ielādē jau ievadītos datus
        
#         self.create_main_page()#paša loga izveides funkcija
    
#     def create_main_page(self):#izveido kalendāru un pogas
#         frame = ttk.Frame(self.root1)#izveido rāmi
#         frame.pack(pady=20, padx=20)#novieto rāmi
        
#         self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")#kalendāru ievieto rāmi(izveido kalendāru)
#         self.calendar.pack()
        
#         self.highlight_dates()

#         view_button = ttk.Button(frame, text="Apskatīt konsultāciju", command=self.view_details)#Poga info apskatīšanai
#         view_button.pack(pady=20)
        
#         add_button = ttk.Button(frame, text="Pievienot/Labot konsultāciju", command=self.open_input_page)
#         add_button.pack(pady=20)
#         izrakstisanas = ttk.Button(root1, text="Izrakstīties", command=self.uzlogu1)
#         izrakstisanas.pack(pady=20)#Izrakstīšanās poga
        
#     def uzlogu1(self):#Funkcija izrakstīšanās pogai
#         root.destroy()#Aizver logu
#         subprocess.call(['python', 'aplikacija.py'])#Atver pierakstīšanās logu

#     def open_input_page(self):#uzpiežot pogu atveras labošanas vai ievadīšanas lapa 
#         input_window = tk.Toplevel(self.root1)
#         input_window.title("Pievienot/Labot konsultāciju")
#         input_window.geometry("300x500")
        
#         ttk.Label(input_window, text="Izvēlieties datumu:").pack()
#         input_calendar = Calendar(input_window, selectmode='day', date_pattern="mm/dd/yyyy")
#         input_calendar.pack()
#         self.highlight_dates(input_calendar)
#         ttk.Label(input_window, text="Ievadiet informāciju:").pack()
#         text_entry = tk.Text(input_window, width=40, height=5)
#         #os.environ["text_entry1"]=text_entry
#         text_entry.pack()
        
#         def load_existing_info():
#             date = input_calendar.get_date()
#             text_entry.delete("1.0", tk.END)
#             text_entry.insert("1.0", self.data.get(date, ""))
        
#         load_existing_info()  # Load existing info for the initially selected date
        
#         def save_data():
#             date = input_calendar.get_date()
#             info = text_entry.get("1.0", tk.END).strip()
#             if info:
#                 self.data[date] = info
#                 self.save_data()
#                 self.highlight_dates()
#                 messagebox.showinfo("Viss izdevies", "Informācija veiksmīgi pievienota!")
#                 input_window.destroy()
#             else:
#                 messagebox.showwarning("Kļūda", "Ievadīta kļūdaina informācija!")
        
#         input_calendar.bind("<<CalendarSelected>>", lambda e: load_existing_info())
        
#         save_button = ttk.Button(input_window, text="Saglabāt", command=save_data)#Informācijas saglabāšanas poga
#         save_button.pack(pady=5)

    
    
#     def view_details(self):
#         selected_date = self.calendar.get_date()
#         info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")
        
#         details_window = tk.Toplevel(self.root1)
#         details_window.geometry("300x500")
#         details_window.title(f"Informācija {selected_date}")
        
#         ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
#         ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
        
#         ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)
        
#     def highlight_dates(self, calendar_widget=None):
#         calendar_widget = calendar_widget or self.calendar  # Clear previous highlights
#         calendar_widget.calevent_remove('all')
#         # Configure event tag for highlighting
#         calendar_widget.tag_config("reminder", background="yellow", foreground="black")

#         for date_str in self.data.keys():
#             try:
#                 # Convert string date to datetime object
#                 date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
#                 # Ensure date is correctly added to the calendar
#                 calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")
#             except ValueError:
#                 continue  # Skip invalid date formats

#         calendar_widget.update_idletasks()  # Refresh UI to show highlights
    

#     def save_data(self):
#         with open(self.data_file, "w") as file:
#             json.dump(self.data, file)
    
#     def load_data(self):
#         try:
#             with open(self.data_file, "r") as file:
#                 return json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return {}
    
# root.mainloop()




# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# import csv
# import subprocess#pip install tkcalendar
# from PIL import Image, ImageTk

# def start_move(event):
    
#     Logs.x = event.x_logs
#     Logs.y = event.y_logs

# def move_window(event):
    
#     dx = event.x_logs - Logs.x  
#     dy = event.y_logs - Logs.y  
#     x = Logs.winfo_x() + dx
#     y = Logs.winfo_y() + dy
#     Logs.geometry(f"+{x}+{y}") 
#     Logs.x = event.x_logs 
#     Logs.y = event.y_logs

# Logs=tk.Tk()# loga objekts
# Logs.title("Mācību konsultācijas")
# Logs.geometry("300x500")
# Logs.configure(background="#f9f9f9")
# Logs.overrideredirect(True)

# title_bar = tk.Frame(Logs, bg="#98c41c", relief="raised", bd=2)
# title_bar.pack(side="top", fill="x")

# title_label = tk.Label(title_bar, text="Mācību konsultācijas", font=("Roboto",12,"bold"), bg="#98c41c", fg="#f9f9f9")
# title_label.pack(side="left", padx=10)

# close_button = tk.Button(title_bar, text="X", bg="red", fg="#f9f9f9", command=Logs.destroy)
# close_button.pack(side="right", padx=5)

# title_bar.bind("<Button-1>", start_move)  # Capture initial position
# title_bar.bind("<B1-Motion>", move_window)  # Move window when dragging

# content_frame = tk.Frame(Logs, bg="#f9f9f9")
# content_frame.pack(fill="both", expand=True)

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

# ttk.Label(Logs, text="Lietotājvārds",font="Arial 20",background='#f9f9f9').pack(pady=14)
# username_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
# username_entry.pack(pady=14)
# ttk.Label(Logs, text="Parole",font="Arial 20",background='#f9f9f9').pack(pady=14)
# password_entry = ttk.Entry(Logs, font="Arial",background='#f9f9f9')
# password_entry = ttk.Entry(Logs, show="*")#Ievadot paroli rāda "*" simbolu vietā
# password_entry.pack(pady=14)

# tk.Button(Logs, text="Pieslēgties",font="Arial",bd=5, command=login,fg="green").pack(pady=14)

# foto_frame=tk.Frame(Logs, background='#f9f9f9')
# foto_frame.pack(pady=14)
# foto_image=Image.open("Kekavas vidusskola-870x1110_11.png")
# resized_foto=foto_image.resize((100,120))
# foto = ImageTk.PhotoImage(resized_foto)
# foto_label=ttk.Label(foto_frame,image=foto, background='#f9f9f9')
# foto_label.pack(pady=14)

# Logs.mainloop()


# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# import subprocess
# import calendar
# from datetime import date
# import datetime
# from tkcalendar import Calendar
# import json
# import os

# class CalendarApp:#izveido klasi
#     def __init__(self, root):#izveido jaunu logu
#         self.root = root#pārdēvē logu
#         self.root.title("Konsultāciju kalendārs")#loga nosaukums
#         root.geometry("300x500")#loga izmēri
#         self.root.overrideredirect(True)

#         self.start_x = 0
#         self.start_y = 0

#         self.title_bar = tk.Frame(root, bg="#98c41c", relief="raised", bd=2)
#         self.title_bar.pack(side="top", fill="x")

#         self.title_label = tk.Label(self.title_bar, text="Konsultāciju kalendārs", font=("Roboto", 12, "bold"), bg="#98c41c", fg="white")
#         self.title_label.pack(side="left", padx=10)

#         self.close_button = tk.Button(self.title_bar, text="Aizvērt", font=("Roboto", 8, "bold"), bg="red", fg="white", bd=3, command=root.destroy)
#         self.close_button.pack(side="right", padx=5, pady=1)
        
#         self.title_bar.bind("<Button-1>", self.start_move)
#         self.title_bar.bind("<B1-Motion>", self.move_window)

#         self.data_file = "calendar_data.json"#atver jau ievadītos vai izveido jaunu failu kur saglabāsies dati
#         self.data = self.load_data()#pievieno funkciju., kurā ielādē jau ievadītos datus
        
#         self.create_main_page()#paša loga izveides funkcija

#     def start_move(self, event):
#         self.start_x = event.x_root - self.root.winfo_x()
#         self.start_y = event.y_root - self.root.winfo_y()

#     def move_window(self, event):
#         x = event.x_root - self.start_x
#         y = event.y_root - self.start_y
#         self.root.geometry(f"+{x}+{y}")
    
#     def create_main_page(self):#izveido kalendāru un pogas
#         frame = ttk.Frame(self.root)#izveido rāmi
#         frame.pack(pady=20, padx=20)#novieto rāmi
        
#         self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")#kalendāru ievieto rāmi(izveido kalendāru)
#         self.calendar.pack()
        
#         self.highlight_dates()

#         view_button = ttk.Button(frame, text="Apskatīt konsultāciju", command=self.view_details)#Poga info apskatīšanai
#         view_button.pack(pady=20)

#         izrakstisanas = ttk.Button(root, text="Izrakstīties", command=self.uzlogu1)
#         izrakstisanas.pack(pady=20)#Izrakstīšanās poga
        
#     def uzlogu1(self):#Funkcija izrakstīšanās pogai
#         root.destroy()#Aizver logu
#         subprocess.call(['python', 'aplikacija.py'])#Atver pierakstīšanās logu
    
#     def view_details(self):
#         selected_date = self.calendar.get_date()
#         info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")
        
#         details_window = tk.Toplevel(self.root)
#         details_window.geometry("300x500")
#         details_window.title(f"Informācija {selected_date}")

#         self.details_window = details_window

#         ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
#         ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
#         ttk.Button(details_window, text="Pieteikties", command=self.pieteikties).pack(pady=10)
#         ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)
        
        
#     def pieteikties(self):
#     # Aizver "Apskatīt konsultāciju" logu
#         if hasattr(self, 'details_window') and self.details_window:
#             self.details_window.destroy()  # Aizver "Apskatīt konsultāciju" logu
    
#         selected_date = self.calendar.get_date()
#         pieteikties_logs  = tk.Toplevel(self.root)
#         pieteikties_logs.geometry("300x500")
#         pieteikties_logs.title(f"Pieteikšanās {selected_date}")

#     # Ievades lauki vārdiem, uzvārdiem un konsultācijas tēmai
#         ttk.Label(pieteikties_logs, text="Vārds:").pack(pady=5)
#         vards_entry = ttk.Entry(pieteikties_logs)
#         vards_entry.pack(pady=5)

#         ttk.Label(pieteikties_logs, text="Uzvārds:").pack(pady=5)
#         uzvards_entry = ttk.Entry(pieteikties_logs)
#         uzvards_entry.pack(pady=5)

#         ttk.Label(pieteikties_logs, text="Konsultācijas tēma:").pack(pady=5)
#         temats_entry = ttk.Entry(pieteikties_logs)
#         temats_entry.pack(pady=5)

#     # Funkcija, lai saglabātu pieteikšanos
#         def save_pieteikums():
#             #konsultacija =
#             #text_entry1 = os.getenv("text_entry1", text_entry)
#             vards = vards_entry.get()
#             uzvards = uzvards_entry.get()
#             temats = temats_entry.get()

#             if not vards or not uzvards or not temats:
#                 messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus!")
#                 return

#         # Saglabā pieteikšanās informāciju JSON failā
#             pieteikums = {
#                 "vards": vards,
#                 "uzvards": uzvards,
#                 "temats": temats
#             }

#         # Nodrošina, ka self.data[selected_date] ir saraksts, ja tas vēl nav
#             if selected_date not in self.data or not isinstance(self.data[selected_date], list):
#                 self.data[selected_date] = []  # Ja nav saraksta, izveido tukšu sarakstu

#             self.data[selected_date].append(pieteikums)  # Pievieno pieteikumu sarakstam

#         # Saglabā datus
#             self.save_data()

#             messagebox.showinfo("Pieteikšanās apstiprinājums", f"Pieteikšanās veiksmīgi saglabāta datumam {selected_date}!")
#             pieteikties_logs.destroy()

#     # Poga, lai saglabātu pieteikšanos
#         ttk.Button(pieteikties_logs, text="Pieteikties", command=save_pieteikums).pack(pady=10)

#     # Poga, lai aizvērtu logu
#         ttk.Button(pieteikties_logs, text="Aizvērt", command=pieteikties_logs.destroy).pack(pady=5)





#     def highlight_dates(self, calendar_widget=None):
#         calendar_widget = calendar_widget or self.calendar  
#         calendar_widget.calevent_remove('all')
#         calendar_widget.tag_config("reminder", background="yellow", foreground="black")

#         for date_str in self.data.keys():
#             try:
#                 date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
#                 calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")
#             except ValueError:
#                 continue  # Izlaiž nepareizi formatētos datumus

#         calendar_widget.update_idletasks()  
    

#     def save_data(self):
#         with open(self.data_file, "w") as file:
#             json.dump(self.data, file)
    
#     def load_data(self):
#         try:
#             with open(self.data_file, "r") as file:
#                 return json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return {}

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CalendarApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import calendar
from datetime import date
import datetime
from tkcalendar import Calendar
import json
import os


class CalendarApp:#izveido klasi
    def __init__(self, root):#izveido jaunu logu
        self.root = root#pārdēvē logu
        self.root.title("Konsultāciju kalendārs")#loga nosaukums
        root.geometry("300x500")#loga izmēri
        self.root.overrideredirect(True)  

        
        self.start_x = 0
        self.start_y = 0

        
        self.title_bar = tk.Frame(root, bg="#98c41c", relief="raised", bd=2)
        self.title_bar.pack(side="top", fill="x")

        self.title_label = tk.Label(self.title_bar, text="Mācību konsultācijas", font=("Roboto", 12, "bold"), bg="#98c41c", fg="#f9f9f9")
        self.title_label.pack(side="left", padx=10)

        self.close_button = tk.Button(self.title_bar, text="Aizvērt", bg="red", font=("Roboto", 8, "bold"), bd=3,fg="#f9f9f9", command=root.destroy)
        self.close_button.pack(side="right", padx=5,pady=1)

        
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.move_window)

        self.data_file = "calendar_data.json"#atver jau ievadītos vai izveido jaunu failu kur saglabāsies dati
        self.data = self.load_data()#pievieno funkciju., kurā ielādē jau ievadītos datus
        
        self.create_main_page()#paša loga izveides funkcija

    def start_move(self, event):
        self.start_x = event.x_root - self.root.winfo_x()
        self.start_y = event.y_root - self.root.winfo_y()

    def move_window(self, event):
        x = event.x_root - self.start_x
        y = event.y_root - self.start_y
        self.root.geometry(f"+{x}+{y}")

    def create_main_page(self):#izveido kalendāru un pogas
        frame = ttk.Frame(self.root)#izveido rāmi
        frame.pack(pady=20, padx=20)#novieto rāmi
        
        self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")#kalendāru ievieto rāmi(izveido kalendāru)
        self.calendar.pack()
        
        self.highlight_dates()

        view_button = ttk.Button(frame, text="Apskatīt konsultāciju", command=self.view_details)#Poga info apskatīšanai
        view_button.pack(pady=20)

        add_button = ttk.Button(frame, text="Pieteikties konsultācijai", command=self.open_input_page)
        add_button.pack(pady=20)

        izrakstisanas = ttk.Button(root, text="Izrakstīties", command=self.uzlogu1)
        izrakstisanas.pack(pady=20)#Izrakstīšanās poga
        
    def uzlogu1(self):#Funkcija izrakstīšanās pogai
        root.destroy()#Aizver logu
        subprocess.call(['python', 'aplikacija.py'])#Atver pierakstīšanās logu
    
    def view_details(self):
        selected_date = self.calendar.get_date()
        info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")
        
        details_window = tk.Toplevel(self.root)
        details_window.geometry("300x500")

        self.root.overrideredirect(True)  

        
        self.start_x = 0
        self.start_y = 0

        
        self.title_bar = tk.Frame(root, bg="#98c41c", relief="raised", bd=2)
        self.title_bar.pack(side="top", fill="x")

        self.title_label = tk.Label(self.title_bar, text=("Mācību konsultācijas",selected_date), font=("Roboto", 12, "bold"), bg="#98c41c", fg="#f9f9f9")
        self.title_label.pack(side="left", padx=10)

        self.close_button = tk.Button(self.title_bar, text="Aizvērt", bg="red", font=("Roboto", 8, "bold"), bd=3,fg="#f9f9f9", command=root.destroy)
        self.close_button.pack(side="right", padx=5,pady=1)

        
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.move_window)

        self.details_window = details_window

        def start_move(self, event):
        self.start_x = event.x_root - self.root.winfo_x()
        self.start_y = event.y_root - self.root.winfo_y()

    def move_window(self, event):
        x = event.x_root - self.start_x
        y = event.y_root - self.start_y
        self.root.geometry(f"+{x}+{y}")



        ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
        ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)
        
        
    def open_input_page(self):#uzpiežot pogu atveras labošanas vai ievadīšanas lapa 
        input_window = tk.Toplevel(self.root)
        input_window.title("Pieteikties konsultācijai")
        input_window.geometry("300x500")
        
        ttk.Label(input_window, text="Izvēlieties datumu:").pack()
        input_calendar = Calendar(input_window, selectmode='day', date_pattern="mm/dd/yyyy")
        input_calendar.pack()
        self.highlight_dates(input_calendar)
        ttk.Label(input_window, text="Pieteikties konsultācijai (vārds, uzvārds, ko vēlies darīt)").pack()
        text_entry = tk.Text(input_window, width=40, height=5)
        #os.environ["text_entry1"]=text_entry
        text_entry.pack()

        
        
        def load_existing_info():
            date = input_calendar.get_date()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", self.data.get(date, ""))
        
        load_existing_info()  # Parāda info izvēlētajam datumam
        
        def save_data():
            date = input_calendar.get_date()
            info = text_entry.get("1.0", tk.END).strip()
            if info:
                self.data[date] = info
                self.save_data()
                self.highlight_dates()
                messagebox.showinfo("Viss izdevies", "Informācija veiksmīgi pievienota!")
                input_window.destroy()
            else:
                messagebox.showwarning("Kļūda", "Ievadīta kļūdaina informācija!")
        
        input_calendar.bind("<<CalendarSelected>>", lambda e: load_existing_info())
        
        save_button = ttk.Button(input_window, text="Saglabāt", command=save_data)#Informācijas saglabāšanas poga
        save_button.pack(pady=5)





    def highlight_dates(self, calendar_widget=None):
        calendar_widget = calendar_widget or self.calendar  
        calendar_widget.calevent_remove('all')
        calendar_widget.tag_config("atg", background="yellow", foreground="black")

        for date_str in self.data.keys():
            try:
                date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
                calendar_widget.calevent_create(date_obj, "Saglabātais info", "atg")
            except ValueError:
                continue  # Izlaiž nepareizi formatētos datumus

        calendar_widget.update_idletasks()  
    

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)
    
    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()






