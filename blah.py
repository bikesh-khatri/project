import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


root = tk.Tk()
# Function to open the login page
def open_login():
    root.withdraw()
    login_page()

# Function to register a new user
def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    role = role_var.get()  # Get selected role

    if not first_name or not last_name or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (first_name, last_name,email,password,role) VALUES (?, ?, ?, ?, ?)", (first_name, last_name,email,password,role))
            conn.commit()
            login_page()
            
        except sqlite3.IntegrityError:
            messagebox.showerror("Signup failed", "Invalid credentials")

        conn.close()

    # Create the registration window

    root.title("Registration Page")
    root.geometry("850x500")
    root.configure(bg="white")

    # Left side (Logo Panel)
    logo_frame = tk.Frame(root, width=300, height=500, bg="gray")
    logo_frame.pack(side="left", fill="both")

    # Load and place logo image for registration
    try:
        logo = Image.open("abc.png")  # Ensure this file exists
        logo = logo.resize((250, 250), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(logo_frame, image=logo_img, bg="gray")
        logo_label.pack(pady=50)
    except Exception as e:
        print(f"Error loading logo: {e}")

    # Right side (Registration Form)
    form_frame = tk.Frame(root, bg="white")
    form_frame.pack(side="right", expand=True, fill="both", padx=40, pady=20)

    tk.Label(form_frame, text="Register", font=("Arial", 18, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

    entry_first_name = tk.Entry(form_frame, font=("Arial", 12))
    entry_last_name = tk.Entry(form_frame, font=("Arial", 12))
    entry_email = tk.Entry(form_frame, font=("Arial", 12))
    entry_password = tk.Entry(form_frame, font=("Arial", 12), show="*")
    entry_confirm_password = tk.Entry(form_frame, font=("Arial", 12), show="*")

    labels = ["First Name:", "Last Name:", "Email:", "Password:", "Confirm Password:"]
    entries = [entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password]

    for i, (label, entry) in enumerate(zip(labels, entries)):
        tk.Label(form_frame, text=label, font=("Arial", 12), bg="white").grid(row=i+1, column=0, sticky="w", pady=5)
        entry.grid(row=i+1, column=1, pady=5, padx=10)

    # Role selection
    role_var = tk.StringVar(value="student")
    tk.Label(form_frame, text="Register as:", font=("Arial", 12), bg="white").grid(row=6, column=0, sticky="w", pady=5)
    tk.Radiobutton(form_frame, text="admin", variable=role_var, value="admin", bg="white").grid(row=6, column=1, sticky="w")
    tk.Radiobutton(form_frame, text="student", variable=role_var, value="student", bg="white").grid(row=7, column=1, sticky="w")

    tk.Button(form_frame, text="Register", command=register, bg="#4CAF50", fg="white", font=("Arial", 12)).grid(row=8, column=0, columnspan=2, pady=20)

    tk.Label(form_frame, text="Already a member?", font=("Arial", 10), bg="white").grid(row=9, column=0, pady=5, sticky="e")

    btn_login = tk.Button(form_frame, text="Login Here", font=("Arial", 10, "underline"), fg="blue", bg="white", bd=0, cursor="hand2", command=open_login)
    btn_login.grid(row=9, column=1, sticky="w")


def login_page():
    login_win = tk.Toplevel()
    login_win.title("Login Page")
    login_win.geometry("900x500")
    login_win.configure(bg="#f4f4f4")

   
    frame = tk.Frame(login_win, bg="white", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    

    # Add logo for login page
    try:
        login_logo = Image.open("abc.png")  # Ensure this file exists for login page
        login_logo = login_logo.resize((250, 250), Image.Resampling.LANCZOS)
        login_logo_img = ImageTk.PhotoImage(login_logo)
        login_logo_label = tk.Label(frame, image=login_logo_img, bg="white")
        login_logo_label.grid(row=0, column=0, columnspan=2, pady=20)
    except Exception as e:
        print(f"Error loading login logo: {e}")
    
    # Login form fields
    tk.Label(frame, text="Email:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=10, sticky="e")
    entry_email = tk.Entry(frame, font=("Arial", 12))
    entry_email.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Password:", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, pady=10, sticky="e")
    entry_password = tk.Entry(frame, font=("Arial", 12), show="*")
    entry_password.grid(row=2, column=1, pady=10)

    role_var = tk.StringVar(value="student")
    tk.Label(frame, text="Login as:", font=("Arial", 12), bg="white").grid(row=3, column=0, pady=5, sticky="e")
    tk.Radiobutton(frame, text="Admin", variable=role_var, value="admin", bg="white").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(frame, text="Student", variable=role_var, value="student", bg="white").grid(row=4, column=1, sticky="w")

    tk.Button(frame, text="Login", command=check_login, bg="#4CAF50", fg="white", font=("Arial", 12), padx=20, pady=5).grid(row=5, column=0, columnspan=2, pady=20)

    def check_login():
        email = entry_email.get()
        password = entry_password.get()
        role = role_var.get()

        if email == "" or password == "":
            messagebox.showerror("Invalid Input", "Fields must not be empty!")
        else:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE email = ? AND password = ? AND role = ?", (email, password,role))
            user = cursor.fetchone()

            if user:
                open_dashboard(role)
            else:
                messagebox.showerror("Login failed", "Invalid email or password")

            conn.close()

    def open_dashboard(role):
        dashboard = tk.Toplevel()
        dashboard.title(f"{role.capitalize()} Dashboard")
        dashboard.geometry("800x600")
        dashboard.configure(bg="#f0f0f0")

        tk.Label(dashboard, text=f"Welcome, {role.capitalize()}!", font=("Arial", 24, "bold"), bg="#f0f0f0").pack(pady=20)

        if role == "admin":
            actions = ["Manage Students", "Manage Courses", "Generate Reports"]
        else:
            actions = ["View Grades", "Enroll in Courses", "View Schedule"]

        for action in actions:
            tk.Button(dashboard, text=action, font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10).pack(pady=10)

        tk.Button(dashboard, text="Logout", command=lambda: logout(dashboard, login_win), bg="#FF5733", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=20)

    def logout(dashboard, login_window):
        dashboard.destroy()
        login_window.deiconify()

    

root.mainloop()
