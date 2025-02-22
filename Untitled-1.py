import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for handling images

# Function to check login credentials
def check_login():
    username = entry_username.get()
    password = entry_password.get()

    # Predefined username and password
    if username == "admin" and password == "password":
        open_dashboard()  # Open the dashboard if login is successful
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open the dashboard
def open_dashboard():
    root.withdraw()  # Hide the login window

    # Create a new window for the dashboard
    dashboard_window = tk.Toplevel()
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("800x600")
    dashboard_window.configure(bg="#f0f0f0")  # Light gray background

    # Add a fancy title to the dashboard
    label_welcome = tk.Label(
        dashboard_window,
        text="Welcome to the Dashboard!",
        font=("Arial", 24, "bold"),
        bg="#f0f0f0",
        fg="#333333",
    )
    label_welcome.pack(pady=20)

    button_frame = tk.Frame(dashboard_window, bg="#f0f0f0")
    button_frame.pack(pady=20)

    button_style = {
        "font": ("Arial", 14),
        "bg": "#4CAF50",  #  background
        "fg": "white",  # White text
        "bd": 0,  # No border
        "padx": 20,
        "pady": 10,
        "activebackground": "#45a049",  # Darker green when clicked
    }

    button1 = tk.Button(button_frame, text="Profile", **button_style)
    button1.grid(row=0, column=0, padx=10, pady=10)

    button2 = tk.Button(button_frame, text="Settings", **button_style)
    button2.grid(row=0, column=1, padx=10, pady=10)

    button3 = tk.Button(button_frame, text="Reports", **button_style)
    button3.grid(row=0, column=2, padx=10, pady=10)

    # Add a logout button
    button_logout = tk.Button(
        dashboard_window,
        text="Logout",
        command=lambda: logout(dashboard_window),
        bg="#FF5733",  # Red background
        fg="white",
        font=("Arial", 12),
        bd=0,
        padx=10,
        pady=5,
    )
    button_logout.pack(pady=20)

# Function to logout and return to the login page
def logout(dashboard_window):
    dashboard_window.destroy()  # Close the dashboard
    root.deiconify()  # Show the login window again

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.attributes("-fullscreen", True)  # Set the window to full screen

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load the background image
try:
    # Replace "background.jpg" with the path to your image
    bg_image = Image.open("123.png") # Load the image
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)  # Resize to fit the screen
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas to place the background image
    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)

    # Set the background image on the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create a frame on top of the canvas to hold the login widgets
    login_frame = tk.Frame(root, bg="white", bd=2, relief=tk.FLAT)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Add padding and design to the login frame
    login_frame.config(padx=30, pady=20)

    # Add a title to the login section
    label_title = tk.Label(login_frame, text="Login", font=("Arial", 18, "bold"), bg="white")
    label_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Create and place the username label and entry
    label_username = tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="white")
    label_username.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_username = tk.Entry(login_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
    entry_username.grid(row=1, column=1, padx=10, pady=10)

    # Create and place the password label and entry
    label_password = tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="white")
    label_password.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_password = tk.Entry(login_frame, show="*", font=("Arial", 12), bd=2, relief=tk.GROOVE)
    entry_password.grid(row=2, column=1, padx=10, pady=10)

    # Create and place the login button
    button_login = tk.Button(login_frame, text="Login", command=check_login, bg="#4CAF50", fg="white", font=("Arial", 12), bd=0, padx=20, pady=10)
    button_login.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    # Add an exit button to close the full-screen window
    exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 12), bd=0, padx=10, pady=5)
    exit_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)  # Place at top-right corner

except Exception as e:
    print(f"Error loading background image: {e}")
    # Fallback to a plain background if the image fails to load
    root.configure(bg="white")

# Run the application
root.mainloop()