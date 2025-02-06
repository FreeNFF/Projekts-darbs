import customtkinter as ctk

#pip install customtkinter

# Sets the appearance mode of the application
ctk.set_appearance_mode("System")

# Sets the color theme
ctk.set_default_color_theme("green")

def create_app():
    root = ctk.CTk()  # Create main window
    root.title("App")  # Set window title
    root.geometry("200x200")  # Set window size
    return root

if __name__ == "__main__":
    app = create_app()
    app.mainloop()