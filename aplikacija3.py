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
        self.data_file = "calendar_data.json"#atver jau ievadītos vai izveido jaunu failu kur saglabāsies dati
        self.data = self.load_data()#pievieno funkciju., kurā ielādē jau ievadītos datus
        
        self.create_main_page()#paša loga izveides funkcija
    
    def create_main_page(self):#izveido kalendāru un pogas
        frame = ttk.Frame(self.root)#izveido rāmi
        frame.pack(pady=20, padx=20)#novieto rāmi
        
        self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")#kalendāru ievieto rāmi(izveido kalendāru)
        self.calendar.pack()
        
        self.highlight_dates()

        view_button = ttk.Button(frame, text="Apskatīt konsultāciju", command=self.view_details)#Poga info apskatīšanai
        view_button.pack(pady=20)
        
        add_button = ttk.Button(frame, text="Pievienot/Labot konsultāciju", command=self.open_input_page)
        add_button.pack(pady=20)
        izrakstisanas = ttk.Button(root, text="Izrakstīties", command=self.uzlogu1)
        izrakstisanas.pack(pady=20)#Izrakstīšanās poga
        
    def uzlogu1(self):#Funkcija izrakstīšanās pogai
        root.destroy()#Aizver logu
        subprocess.call(['python', 'aplikacija.py'])#Atver pierakstīšanās logu

    def open_input_page(self):#uzpiežot pogu atveras labošanas vai ievadīšanas lapa 
        input_window = tk.Toplevel(self.root)
        input_window.title("Pievienot/Labot konsultāciju")
        input_window.geometry("300x500")
        
        ttk.Label(input_window, text="Izvēlieties datumu:").pack()
        input_calendar = Calendar(input_window, selectmode='day', date_pattern="mm/dd/yyyy")
        input_calendar.pack()
        self.highlight_dates(input_calendar)
        ttk.Label(input_window, text="Ievadiet informāciju:").pack()
        text_entry = tk.Text(input_window, width=40, height=5)
        #os.environ["text_entry1"]=text_entry
        text_entry.pack()
        
        def load_existing_info():
            date = input_calendar.get_date()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", self.data.get(date, ""))
        
        load_existing_info()  # Load existing info for the initially selected date
        
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

    
    
    def view_details(self):
        selected_date = self.calendar.get_date()
        info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")
        
        details_window = tk.Toplevel(self.root)
        details_window.geometry("300x500")
        details_window.title(f"Informācija {selected_date}")
        
        ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
        
        ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)
        
    def highlight_dates(self, calendar_widget=None):
        calendar_widget = calendar_widget or self.calendar  # Clear previous highlights
        calendar_widget.calevent_remove('all')
        # Configure event tag for highlighting
        calendar_widget.tag_config("reminder", background="yellow", foreground="black")

        for date_str in self.data.keys():
            try:
                # Convert string date to datetime object
                date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
                # Ensure date is correctly added to the calendar
                calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")
            except ValueError:
                continue  # Skip invalid date formats

        calendar_widget.update_idletasks()  # Refresh UI to show highlights
    

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
