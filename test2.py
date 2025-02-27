# import tkinter as tk  # Import Tkinter for GUI creation
# from tkinter import ttk, messagebox  # Import themed widgets and messagebox for displaying alerts
# import subprocess  # Import subprocess to execute external scripts
# import datetime  # Import datetime module to work with dates
# from tkcalendar import Calendar  # Import Calendar widget from tkcalendar
# import json  # Import JSON module to save and load data

# class CalendarApp:
#     def __init__(self, root):  # Initialize the calendar application
#         self.root = root  # Assign the main application window
#         self.root.title("Konsultāciju kalendārs")  # Set window title
#         root.geometry("300x500")  # Set window size
#         self.data_file = "calendar_data.json"  # Define the file to store consultation data
#         self.data = self.load_data()  # Load previously saved data
        
#         self.create_main_page()  # Create the main page UI
    
#     def create_main_page(self):  # Create the main calendar page
#         frame = ttk.Frame(self.root)  # Create a frame to hold widgets
#         frame.pack(pady=20, padx=20)  # Pack the frame with padding
        
#         self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")  # Create a calendar widget
#         self.calendar.pack()  # Display the calendar
        
#         self.highlight_dates()  # Highlight dates that have saved consultations

#         view_button = ttk.Button(frame, text="Apskatīt konsultāciju", command=self.view_details)  # Button to view consultation details
#         view_button.pack(pady=20)  # Display the button
        
#         add_button = ttk.Button(frame, text="Pievienot/Labot konsultāciju", command=self.open_input_page)  # Button to add/edit consultations
#         add_button.pack(pady=20)  # Display the button
        
#         izrakstisanas = ttk.Button(root, text="Izrakstīties", command=self.uzlogu1)  # Button to log out
#         izrakstisanas.pack(pady=20)  # Display the button
    
#     def uzlogu1(self):  # Function to log out
#         root.destroy()  # Close the current window
#         subprocess.call(['python', 'aplikacija.py'])  # Open the login script

#     def open_input_page(self):  # Open a new window to add or edit consultations
#         input_window = tk.Toplevel(self.root)  # Create a new top-level window
#         input_window.title("Pievienot/Labot konsultāciju")  # Set title
#         input_window.geometry("300x500")  # Set window size

#         ttk.Label(input_window, text="Izvēlieties datumu:").pack()  # Label for date selection
#         input_calendar = Calendar(input_window, selectmode='day', date_pattern="mm/dd/yyyy")  # Create calendar widget
#         input_calendar.pack()  # Display the calendar
        
#         self.highlight_dates(input_calendar)  # Highlight dates with existing consultations

#         ttk.Label(input_window, text="Ievadiet informāciju:").pack()  # Label for input field
#         text_entry = tk.Text(input_window, width=40, height=5)  # Create text entry field
#         text_entry.pack()  # Display the text field
        
#         def load_existing_info():  # Load existing consultation data for the selected date
#             date = input_calendar.get_date()  # Get selected date
#             text_entry.delete("1.0", tk.END)  # Clear text field
#             text_entry.insert("1.0", self.data.get(date, ""))  # Insert saved data if available
        
#         load_existing_info()  # Load existing info initially
        
#         def save_data():  # Function to save consultation data
#             date = input_calendar.get_date()  # Get selected date
#             info = text_entry.get("1.0", tk.END).strip()  # Get entered text
#             if info:  # Check if text is not empty
#                 self.data[date] = info  # Save data
#                 self.save_data()  # Write data to file
#                 self.highlight_dates()  # Refresh highlighted dates
#                 messagebox.showinfo("Viss izdevies", "Informācija veiksmīgi pievienota!")  # Show success message
#                 input_window.destroy()  # Close the input window
#             else:
#                 messagebox.showwarning("Kļūda", "Ievadīta kļūdaina informācija!")  # Show warning if no data entered
        
#         input_calendar.bind("<<CalendarSelected>>", lambda e: load_existing_info())  # Update text field when a new date is selected
        
#         save_button = ttk.Button(input_window, text="Saglabāt", command=save_data)  # Button to save consultation info
#         save_button.pack(pady=5)  # Display the button
    
#     def view_details(self):  # Function to display consultation details
#         selected_date = self.calendar.get_date()  # Get selected date
#         info = self.data.get(selected_date, "Nav konsultācija šajā datumā!")  # Retrieve info for the date
        
#         details_window = tk.Toplevel(self.root)  # Create a new window for details
#         details_window.title(f"Informācija {selected_date}")  # Set title
        
#         ttk.Label(details_window, text=f"Datums: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)  # Display date
#         ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)  # Display consultation details
        
#         ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=20)  # Button to close the window
    
#     def highlight_dates(self, calendar_widget=None):  # Highlight dates with consultations
#         calendar_widget = calendar_widget or self.calendar  # Use provided calendar widget or default
#         calendar_widget.calevent_remove('all')  # Clear previous highlights
#         calendar_widget.tag_config("reminder", background="yellow", foreground="black")  # Set highlight style

#         for date_str in self.data.keys():  # Loop through saved consultation dates
#             try:
#                 date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()  # Convert string to date object
#                 calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")  # Highlight date
#             except ValueError:
#                 continue  # Skip invalid dates
        
#         calendar_widget.update_idletasks()  # Refresh calendar UI
    
#     def save_data(self):  # Save consultation data to JSON file
#         with open(self.data_file, "w") as file:
#             json.dump(self.data, file)  # Write data to file
    
#     def load_data(self):  # Load consultation data from JSON file
#         try:
#             with open(self.data_file, "r") as file:
#                 return json.load(file)  # Read and return data
#         except (FileNotFoundError, json.JSONDecodeError):
#             return {}  # Return empty dictionary if file not found or invalid

# if __name__ == "__main__":  # Run application if script is executed directly
#     root = tk.Tk()  # Create the main application window
#     app = CalendarApp(root)  # Initialize CalendarApp
#     root.mainloop()  # Start the Tkinter event loop





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
        ttk.Label(input_window, text="Labot informāciju:").pack()
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

        # ttk.Label(input_window, text="Pievienot konsultāciju").pack(pady=5)
        # New_consultation = ttk.Entry(input_window)
        # New_consultation.pack()
        # button_save = ttk.Button(input_window, text="Pievienot")#, command=data_save)#Informācijas saglabāšanas poga
        # button_save.pack(pady=5)

        # def data_save():
        #     date = input_calendar.get_date()
        #     info = New_consultation.get("1.0", tk.END).strip()
        #     if info:
        #         self.data[date] = info
        #         self.save_data()
        #         self.highlight_dates()
        #         messagebox.showinfo("Viss izdevies", "Informācija veiksmīgi pievienota!")
        #         input_window.destroy()
        #     else:
        #         messagebox.showwarning("Kļūda", "Ievadīta kļūdaina informācija!")

    
    
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
        calendar_widget = calendar_widget or self.calendar  
        calendar_widget.calevent_remove('all')
        calendar_widget.tag_config("reminder", background="yellow", foreground="black")

        for date_str in self.data.keys():
            try:
                date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
                #Pārbauda vai info pievienots pareizi kalendārām
                calendar_widget.calevent_create(date_obj, "Saved Info", "reminder")
            except ValueError:
                continue  # Izlaiž nepareizi formatētos datumus

        calendar_widget.update_idletasks()  
    

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)
        
    # def data_save(self):
    #     with open(self.data_file, "w") as file:
    #         json.dump(self.data, file)
    
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


