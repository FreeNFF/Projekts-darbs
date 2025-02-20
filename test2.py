import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import json
import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Information App")

        self.data_file = "calendar_data.json"
        self.data = self.load_data()

        self.create_main_page()

    def create_main_page(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20)

        self.calendar = Calendar(frame, selectmode='day', date_pattern="mm/dd/yyyy")
        self.calendar.pack()

        self.highlight_dates()  # Highlight saved dates

        view_button = ttk.Button(frame, text="View Details", command=self.view_details)
        view_button.pack(pady=5)

        add_button = ttk.Button(frame, text="Add Information", command=self.open_input_page)
        add_button.pack(pady=5)

    def open_input_page(self):
        input_window = tk.Toplevel(self.root)
        input_window.title("Add Information")

        ttk.Label(input_window, text="Select Date:").pack()
        input_calendar = Calendar(input_window, selectmode='day', date_pattern="mm/dd/yyyy")
        input_calendar.pack()

        ttk.Label(input_window, text="Enter Information:").pack()
        text_entry = tk.Text(input_window, width=40, height=5)
        text_entry.pack()

        def load_existing_info():
            date = input_calendar.get_date()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", self.data.get(date, ""))

        load_existing_info()  # Load info for the initially selected date

        def save_data():
            date = input_calendar.get_date()
            info = text_entry.get("1.0", tk.END).strip()
            if info:
                self.data[date] = info
                self.save_data()  # Save data to file
                self.highlight_dates()  # Update main calendar highlights
                messagebox.showinfo("Success", "Information saved successfully!")
                input_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter some information")

        input_calendar.bind("<<CalendarSelected>>", lambda e: load_existing_info())

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

    def highlight_dates(self):
        self.calendar.calevent_remove('all')  # Clear previous highlights

        # Configure event tag for highlighting
        self.calendar.tag_config("reminder", background="yellow", foreground="black")

        for date_str in self.data.keys():
            try:
                # Convert string date to datetime object
                date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
                
                # Ensure date is correctly added to the calendar
                self.calendar.calevent_create(date_obj, "Saved Info", "reminder")
            except ValueError:
                continue  # Skip invalid date formats

        self.calendar.update_idletasks()  # Refresh UI to show highlights

    def save_data(self):
        """Saves user input to a JSON file."""
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)

    def load_data(self):
        """Loads data from JSON file (or creates a new one if missing)."""
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
