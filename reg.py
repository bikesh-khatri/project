import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to handle registration logic
def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not first_name or not last_name or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        messagebox.showinfo("Success", "Registration successful!")

# Function to open login page (for now, just a message)
def open_login():
    messagebox.showinfo("Redirect", "Redirecting to Login Page...")  # Replace with actual login window

# Create main window
root = tk.Tk()
root.title("Registration Page")
root.geometry("850x500")
root.configure(bg="white")

# Left side (Logo Panel)
logo_frame = tk.Frame(root, width=300, height=500, bg="gray")
logo_frame.pack(side="left", fill="both")

# Load and place logo image
try:
    logo = Image.open("abc.png")  # Use your logo file
    logo = logo.resize((250, 250), Image.Resampling.LANCZOS)
    logo_img = ImageTk.PhotoImage(logo)
    
    logo_label = tk.Label(logo_frame, image=logo_img, bg="gray")
    logo_label.pack(pady=50)
except Exception as e:
    print(f"Error loading logo: {e}")

# Right side (Registration Form)
form_frame = tk.Frame(root, bg="white")
form_frame.pack(side="right", expand=True, fill="both", padx=40, pady=20)

# Registration Title
label_title = tk.Label(form_frame, text="Register", font=("Arial", 18, "bold"), bg="white")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# First Name
tk.Label(form_frame, text="First Name:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w", pady=5)
entry_first_name = tk.Entry(form_frame, font=("Arial", 12))
entry_first_name.grid(row=1, column=1, pady=5, padx=10)

# Last Name
tk.Label(form_frame, text="Last Name:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="w", pady=5)
entry_last_name = tk.Entry(form_frame, font=("Arial", 12))
entry_last_name.grid(row=2, column=1, pady=5, padx=10)

# Email
tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="w", pady=5)
entry_email = tk.Entry(form_frame, font=("Arial", 12))
entry_email.grid(row=3, column=1, pady=5, padx=10)

# Password
tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="white").grid(row=4, column=0, sticky="w", pady=5)
entry_password = tk.Entry(form_frame, font=("Arial", 12), show="*")
entry_password.grid(row=4, column=1, pady=5, padx=10)

# Confirm Password
tk.Label(form_frame, text="Confirm Password:", font=("Arial", 12), bg="white").grid(row=5, column=0, sticky="w", pady=5)
entry_confirm_password = tk.Entry(form_frame, font=("Arial", 12), show="*")
entry_confirm_password.grid(row=5, column=1, pady=5, padx=10)

# Register Button
btn_register = tk.Button(form_frame, text="Register", command=register, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_register.grid(row=6, column=0, columnspan=2, pady=20)

# Already a Member? Login Link
label_login = tk.Label(form_frame, text="Already a member?", font=("Arial", 10), bg="white")
label_login.grid(row=7, column=0, pady=5, sticky="e")

btn_login = tk.Button(form_frame, text="Login Here", font=("Arial", 10, "underline"), fg="blue", bg="white", bd=0, cursor="hand2", command=open_login)
btn_login.grid(row=7, column=1, sticky="w")

root.mainloop()
