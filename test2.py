import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Information App")
        
        self.data = {}  # Dictionary to store date-wise data
        
        self.create_main_page()
    
    def create_main_page(self):#izveido jaunu logu, kurā ir iespēja redzēt datumus un 
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20)
        
        self.calendar = Calendar(frame, selectmode='day')
        self.calendar.pack()
        
        view_button = ttk.Button(frame, text="View Details", command=self.view_details)
        view_button.pack(pady=5)
        
        add_button = ttk.Button(frame, text="Add Information", command=self.open_input_page)
        add_button.pack(pady=5)
    
    def open_input_page(self):
        input_window = tk.Toplevel(self.root)
        input_window.title("Add Information")
        
        ttk.Label(input_window, text="Select Date:").pack()
        input_calendar = Calendar(input_window, selectmode='day')
        input_calendar.pack()
        
        ttk.Label(input_window, text="Enter Information:").pack()
        text_entry = tk.Text(input_window, width=40, height=5)
        text_entry.pack()
        
        def save_data():
            date = input_calendar.get_date()
            info = text_entry.get("1.0", tk.END).strip()
            if info:
                self.data[date] = info
                messagebox.showinfo("Success", "Information saved successfully!")
                input_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter some information")
        
        save_button = ttk.Button(input_window, text="Save", command=save_data)
        save_button.pack(pady=5)
    
    def view_details(self):
        selected_date = self.calendar.get_date()
        info = self.data.get(selected_date, "No information available for this date.")
        
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Details for {selected_date}")
        
        ttk.Label(details_window, text=f"Date: {selected_date}", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(details_window, text=info, wraplength=300, justify="left").pack(pady=5)
        
        ttk.Button(details_window, text="Close", command=details_window.destroy).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
