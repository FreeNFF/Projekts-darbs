#pievieno nepieciešamās bibliotēkas
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



class CalendarApp:#izveido klasi
    def __init__(self, root):#izveido jaunu logu
        self.root = root#pārdēvē logu
        self.root.title("Konsultāciju kalendārs")#loga nosaukums
        root.geometry("300x500")#loga izmēri
        self.root.overrideredirect(True)#noņem sākotnējo loga dizainu

        #loga sākumpunkts 
        self.start_x = 0
        self.start_y = 0

        #loga dizainu veidošana
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

    def start_move(self, event):#funkcija ar kuras palīdzību var kustināt (sāk kustināt logu)
        self.start_x = event.x_root - self.root.winfo_x()
        self.start_y = event.y_root - self.root.winfo_y()

    def move_window(self, event):#funkcija, kura kustinot pelīti pakustina logu
        x = event.x_root - self.start_x
        y = event.y_root - self.start_y
        self.root.geometry(f"+{x}+{y}")

    def create_main_page(self):#izveido kalendāru un pogas
        frame = ttk.Frame(self.root)#izveido rāmi
        frame.pack(pady=20, padx=20)#novieto rāmi
        
        self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")#kalendāru ievieto rāmi(izveido kalendāru)
        self.calendar.pack()
        
        self.highlight_dates()#funkcija, kas iekrāso kalendārā konsultācijas datumus

        #pievieno pogas
        view_button = tk.Button(frame, text="Apskatīt konsultāciju",font=("Roboto",10,"bold"),bg="#98c41c",fg="white",bd=3, command=self.view_details)#Poga info apskatīšanai
        view_button.pack(pady=20)

        add_button = tk.Button(frame, text="Pieteikties konsultācijai",font=("Roboto",10,"bold"),bg="#98c41c",fg="white",bd=3, command=self.open_input_page)
        add_button.pack(pady=20)

        izrakstisanas = tk.Button(root, text="Izrakstīties",font=("Roboto",10,"bold"),bg="#98c41c",fg="white",bd=3, command=self.uzlogu1)
        izrakstisanas.pack(pady=20)#Izrakstīšanās poga
        
    def uzlogu1(self):#Funkcija izrakstīšanās pogai
        root.destroy()#Aizver logu
        subprocess.call(['python', 'aplikacija.py'])#Atver pierakstīšanās logu
    
    def view_details(self):#funkcijas, kas izveido logu, kurā var redzēt 
        selected_date = self.calendar.get_date()#iegūst izvēlēto datumu 
        info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")#izvada, ka nav konsultācijas, ja konsultācija nav pieteikta tajā dienā
        #izveido logu, kā arī nomaina izmērus un tā nosakumu
        details_window = tk.Toplevel(self.root)
        details_window.geometry("300x500")
        details_window.title(f"Informācija {selected_date}")

        self.details_window = details_window#pārmaina logu uz nezināmu details_window

        #Logā parāda konsultācijas informāciju, ja nav tad parāda, ka konsultācijas nav
        ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Roboto", 12, "bold")).pack(pady=5)
        ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
        tk.Button(details_window, text="Aizvērt", font=("Roboto",10,"bold"),bg="#98c41c",fg="white",bd=3,command=details_window.destroy).pack(pady=20)
        
        
    def open_input_page(self):#uzpiežot pogu atveras labošanas vai ievadīšanas lapa 
        #izveido jaunu logu
        input_window = tk.Toplevel(self.root)
        input_window.title("Pieteikties konsultācijai")
        input_window.geometry("300x500")
        #pievienu tekstus un kalendāru 
        ttk.Label(input_window, text="Izvēlieties datumu:").pack()
        input_calendar = Calendar(input_window, selectmode='day', date_pattern="mm/dd/yyyy")
        input_calendar.pack()
        self.highlight_dates(input_calendar)#pievieno funkciju, kura iezīmē konsultācijas datumus

        #pievieno vietu, kur ievadīt konsultācijas informāciju
        ttk.Label(input_window, text="Pieteikties konsultācijai (Vārds, uzvārds, ko vēlies darīt)").pack()
        text_entry = tk.Text(input_window, width=40, height=5)
        #os.environ["text_entry1"]=text_entry
        text_entry.pack()

        
        #ielādē iepriekš izveidotās konsultācijas, ja tādas ir.
        def load_existing_info():
            date = input_calendar.get_date()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", self.data.get(date, ""))
        
        load_existing_info()#pievieno funkciju, kura ielādē iepriekš izveidotās konsultācijas, ja tādas ir

        #funkcija, kura saglabā ievadītos datus teksta lodziņā
        def save_data():
            date = input_calendar.get_date()
            info = text_entry.get("1.0", tk.END).strip()

            if info:
                self.data[date] = info
            else:
                self.data.pop(date, None)  # noņem iezīmēto datumu, ja nav nekas ierakstīts teksta lodziņā
            self.save_data()
            self.highlight_dates()
            messagebox.showinfo("Viss izdevies", "Informācija veiksmīgi saglabāta!")
            input_window.destroy()
        
        input_calendar.bind("<<CalendarSelected>>", lambda e: load_existing_info())#Atjaunina teksta lauku, kad ir atlasīts jauns datums
        
        save_button = tk.Button(input_window, text="Saglabāt", font=("Roboto",10,"bold"),bg="#98c41c",fg="white",bd=3, command=save_data)#Informācijas saglabāšanas poga
        save_button.pack(pady=5)





    def highlight_dates(self, calendar_widget=None):#funkcija, ar kuru konsultācijas datumus iezīmē dzeltenā krāsā
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
    

    def save_data(self):#saglabā datus noteiktā failā
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)
    
    def load_data(self):#ielādē datus no šī paša faila
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

if __name__ == "__main__":#funkcija ar kuras palīdzību tiek palaista programma
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
