import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to check login credentials
def check_login(role):
    username = entry_id.get()
    password = entry_password.get()

    # Predefined credentials for admin and student
    if role == "admin":
        if username == "admin" and password == "password":
            open_admin_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid admin credentials")
    elif role == "student":
        if username == "student" and password == "1234":
            open_student_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid student credentials")

# Function to open the admin dashboard
def open_admin_dashboard():
    root.withdraw()  # Hide the login window

    # Create a new window for the admin dashboard
    admin_dashboard = tk.Toplevel()
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.geometry("800x600")
    admin_dashboard.configure(bg="#f0f0f0")

    # Add a welcome message
    tk.Label(
        admin_dashboard,
        text="Welcome, Admin!",
        font=("Arial", 24, "bold"),
        bg="#f0f0f0",
    ).pack(pady=20)

    # Add buttons for admin-specific functionality
    button_frame = tk.Frame(admin_dashboard, bg="#f0f0f0")
    button_frame.pack(pady=20)

    admin_buttons = ["Manage Students", "Manage Courses", "Generate Reports"]
    for i, btn_text in enumerate(admin_buttons):
        tk.Button(
            button_frame,
            text=btn_text,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
        ).grid(row=0, column=i, padx=10, pady=10)

    # Add a logout button
    tk.Button(
        admin_dashboard,
        text="Logout",
        command=lambda: logout(admin_dashboard),
        bg="#FF5733",
        fg="white",
        font=("Arial", 12),
        padx=10,
        pady=5,
    ).pack(pady=20)

# Function to open the student dashboard
def open_student_dashboard():
    root.withdraw()  # Hide the login window

    # Create a new window for the student dashboard
    student_dashboard = tk.Toplevel()
    student_dashboard.title("Student Dashboard")
    student_dashboard.geometry("800x600")
    student_dashboard.configure(bg="#f0f0f0")

    # Add a welcome message
    tk.Label(
        student_dashboard,
        text="Welcome, Student!",
        font=("Arial", 24, "bold"),
        bg="#f0f0f0",
    ).pack(pady=20)

    # Add buttons for student-specific functionality
    button_frame = tk.Frame(student_dashboard, bg="#f0f0f0")
    button_frame.pack(pady=20)

    student_buttons = ["View Grades", "Enroll in Courses", "View Schedule"]
    for i, btn_text in enumerate(student_buttons):
        tk.Button(
            button_frame,
            text=btn_text,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
        ).grid(row=0, column=i, padx=10, pady=10)

    # Add a logout button
    tk.Button(
        student_dashboard,
        text="Logout",
        command=lambda: logout(student_dashboard),
        bg="#FF5733",
        fg="white",
        font=("Arial", 12),
        padx=10,
        pady=5,
    ).pack(pady=20)

# Function to logout and return to the login page
def logout(dashboard_window):
    dashboard_window.destroy()  # Close the dashboard
    root.deiconify()  # Show the login window again

# Function for "Forget Password" functionality
def forget_password():
    messagebox.showinfo("Forget Password", "Please contact the administrator to reset your password.")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("900x500")
root.configure(bg="white")

# Left frame for logo
frame_left = tk.Frame(root, width=400, height=500, bg="black")
frame_left.pack(side="left", fill="y")

# Right frame for login form
frame_right = tk.Frame(root, bg="white", padx=40, pady=20)
frame_right.pack(expand=True, fill="both")

# Load and display the logo
try:
    logo_img = Image.open("abc.png")  # Replace with your logo path
    logo_img = logo_img.resize((300, 300), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    tk.Label(frame_left, image=logo_photo, bg="black").pack(pady=20)
except Exception as e:
    print(f"Error loading logo: {e}")

# Add "Sign In" label
tk.Label(frame_right, text="Sign In", font=("Arial", 18, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

# Add ID field
tk.Label(frame_right, text="ID:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=10, sticky="e")
entry_id = tk.Entry(frame_right, font=("Arial", 12))
entry_id.grid(row=1, column=1, pady=10)

# Add Password field
tk.Label(frame_right, text="PASSWORD:", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, pady=10, sticky="e")
entry_password = tk.Entry(frame_right, font=("Arial", 12), show="*")
entry_password.grid(row=2, column=1, pady=10)

# Add "Login as Admin" button
tk.Button(
    frame_right,
    text="Login as Admin",
    command=lambda: check_login("admin"),
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    padx=20,
    pady=5,
).grid(row=3, column=0, columnspan=2, pady=5)

# Add "Login as Student" button
tk.Button(
    frame_right,
    text="Login as Student",
    command=lambda: check_login("student"),
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    padx=20,
    pady=5,
).grid(row=4, column=0, columnspan=2, pady=5)

# Add "Forget Password" link
forget_password_label = tk.Label(
    frame_right,
    text="Forget Password?",
    font=("Arial", 10),
    fg="blue",
    bg="white",
    cursor="hand2",  # Change cursor to hand on hover
)
forget_password_label.grid(row=5, column=0, columnspan=2, pady=(20, 5))
# Bind the "Forget Password" label to the function
forget_password_label.bind("<Button-1>", lambda e: forget_password())

# Run the application
root.mainloop()