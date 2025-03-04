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
        details_window.title(f"Informācija {selected_date}")

        self.details_window = details_window

        ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
        ttk.Button(details_window, text="Pieteikties", command=self.pieteikties).pack(pady=10)
        ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)
        
        
    def pieteikties(self):
    # Aizver "Apskatīt konsultāciju" logu
        if hasattr(self, 'details_window') and self.details_window:
            self.details_window.destroy()  # Aizver "Apskatīt konsultāciju" logu
    
        selected_date = self.calendar.get_date()
        pieteikties_logs  = tk.Toplevel(self.root)
        pieteikties_logs.geometry("300x500")
        pieteikties_logs.title(f"Pieteikšanās {selected_date}")

    # Ievades lauki vārdiem, uzvārdiem un konsultācijas tēmai
        ttk.Label(pieteikties_logs, text="Vārds:").pack(pady=5)
        vards_entry = ttk.Entry(pieteikties_logs)
        vards_entry.pack(pady=5)

        ttk.Label(pieteikties_logs, text="Uzvārds:").pack(pady=5)
        uzvards_entry = ttk.Entry(pieteikties_logs)
        uzvards_entry.pack(pady=5)

        ttk.Label(pieteikties_logs, text="Konsultācijas tēma:").pack(pady=5)
        temats_entry = ttk.Entry(pieteikties_logs)
        temats_entry.pack(pady=5)

    # Funkcija, lai saglabātu pieteikšanos
        def save_pieteikums():
            #konsultacija =
            #text_entry1 = os.getenv("text_entry1", text_entry)
            vards = vards_entry.get()
            uzvards = uzvards_entry.get()
            temats = temats_entry.get()

            if not vards or not uzvards or not temats:
                messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus!")
                return

        # Saglabā pieteikšanās informāciju JSON failā
            pieteikums = {
                "vards": vards,
                "uzvards": uzvards,
                "temats": temats
            }

        # Nodrošina, ka self.data[selected_date] ir saraksts, ja tas vēl nav
            if selected_date not in self.data or not isinstance(self.data[selected_date], list):
                self.data[selected_date] = []  # Ja nav saraksta, izveido tukšu sarakstu

            self.data[selected_date].append(pieteikums)  # Pievieno pieteikumu sarakstam

        # Saglabā datus
            self.save_data()

            messagebox.showinfo("Pieteikšanās apstiprinājums", f"Pieteikšanās veiksmīgi saglabāta datumam {selected_date}!")
            pieteikties_logs.destroy()

    # Poga, lai saglabātu pieteikšanos
        ttk.Button(pieteikties_logs, text="Pieteikties", command=save_pieteikums).pack(pady=10)

    # Poga, lai aizvērtu logu
        ttk.Button(pieteikties_logs, text="Aizvērt", command=pieteikties_logs.destroy).pack(pady=5)





    def highlight_dates(self, calendar_widget=None):
        calendar_widget = calendar_widget or self.calendar  
        calendar_widget.calevent_remove('all')
        calendar_widget.tag_config("reminder", background="yellow", foreground="black")

        for date_str in self.data.keys():
            try:
                date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
                calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")
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
