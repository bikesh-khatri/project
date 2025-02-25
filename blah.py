import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

def register_page(root):
    """Function to create the registration page"""

    root.withdraw()  # Hide the main root window
    register_win = tk.Toplevel(root)
    register_win.title("Registration Page")
    register_win.geometry("850x500")
    register_win.configure(bg="white")
    register_win.iconbitmap("abc.ico")

    def register():
        """Handles user registration"""
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        email = entry_email.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()
       

        if not first_name or not last_name or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
                           (first_name, last_name, email, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            register_win.destroy()  # Close register window
            login_page(root)  # Open login page after successful registration
        except sqlite3.IntegrityError:
            messagebox.showerror("Signup failed", "Email already exists!")
        finally:
            conn.close()

    logo_frame = tk.Frame(register_win, width=300, height=500, bg="gray")
    logo_frame.pack(side="left", fill="both")

    # Load and place logo image
    try:
        logo = Image.open("abc.png")
        logo = logo.resize((250, 250), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(logo_frame, image=logo_img, bg="gray")
        logo_label.image = logo_img  # Keep reference
        logo_label.pack(pady=50)
    except Exception as e:
        print(f"Error loading logo: {e}")

    form_frame = tk.Frame(register_win, bg="white")
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

    tk.Button(form_frame, text="Register", command=register, bg="#4CAF50", fg="white", font=("Arial", 12)).grid(row=8, column=0, columnspan=2, pady=20)

    tk.Label(form_frame, text="Already a member?", font=("Arial", 10), bg="white").grid(row=9, column=0, pady=5, sticky="e")

    gotoLogin = tk.Button(form_frame, text="Login Here", font=("Arial", 10, "underline"), fg="blue", bg="white", bd=0, cursor="hand2",
                          command=lambda: [register_win.destroy(), login_page(root)])
    gotoLogin.grid(row=9, column=1, sticky="w")


def login_page(root):
    """Function to create the login page"""

    root.withdraw()  # Hide main root window
    login_win = tk.Toplevel(root)
    login_win.title("Login Page")
    login_win.geometry("900x500")
    login_win.configure(bg="#f4f4f4")
    login_win.iconbitmap("abc.ico")
    logo_frame = tk.Frame(login_win, width=300, height=500, bg="gray")
    logo_frame.pack(side="left", fill="both")
    try:
        logo = Image.open("abc.png")
        logo = logo.resize((250, 250), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(logo_frame, image=logo_img, bg="gray")
        logo_label.image = logo_img  # Keep reference
        logo_label.pack(pady=50)
    except Exception as e:
        print(f"Error loading logo: {e}")
    form_frame = tk.Frame(login_win, bg="white")
    form_frame.pack(side="right", expand=True, fill="both", padx=40, pady=20)
    def check_login():
        """Validates user login credentials"""
        email = entry_email.get()
        password = entry_password.get()

        if not email or not password:
            messagebox.showerror("Invalid Input", "Fields must not be empty!")
            return

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            login_win.destroy()  # Close login window
            admin_dashboard()
        else:
            messagebox.showerror("Login failed", "Invalid email or password")

    frame = tk.Frame(login_win, bg="white", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Email:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=10, sticky="e")
    entry_email = tk.Entry(frame, font=("Arial", 12))
    entry_email.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Password:", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, pady=10, sticky="e")
    entry_password = tk.Entry(frame, font=("Arial", 12), show="*")
    entry_password.grid(row=2, column=1, pady=10)

    tk.Button(frame, text="Login", command=check_login, bg="#4CAF50", fg="white", font=("Arial", 12), padx=20, pady=5).grid(row=5, column=0, columnspan=2, pady=20)

    tk.Label(frame, text="Create new account?", font=("Arial", 10), bg="white").grid(row=9, column=0, pady=5, sticky="e")

    gotoRegister = tk.Button(frame, text="Register Here", font=("Arial", 10, "underline"), fg="blue", bg="white", bd=0, cursor="hand2",
                          command=lambda: [login_win.destroy(), register_page(root)])
    gotoRegister.grid(row=9, column=1, sticky="w")


def admin_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Warden Sab")
    dashboard.geometry("800x600")
    dashboard.configure(bg="#f0f0f0")
    dashboard.iconbitmap("abc.ico")

    # Welcome message
    welcome_label = tk.Label(dashboard, text=f"Welcome!", font=("Arial", 24, "bold"), bg="#F0F0F0", fg="black")
    welcome_label.pack(pady=20)

    # Frame to hold buttons 
    button_frame = tk.Frame(dashboard, bg="#f0f0f0")
    button_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Configure columns to allocate extra space
    button_frame.columnconfigure(0, weight=1)  # Left column
    button_frame.columnconfigure(1, weight=1)  # Right column

      # Create big and square buttons
    button_width = 15
    button_height = 5

    # Meal button (top left, below welcome message)
    meal_button = tk.Button(button_frame, text="Meal",  command=lambda: [dashboard.destroy(), meal_management(root)], bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    meal_button.grid(row=1, column=0, padx=50, pady=20, sticky="nw")  # Added padx for spacing

    
    # Student button (below meal)
    student_button = tk.Button(button_frame, text="Students",  command=lambda: [dashboard.destroy(), students(root)], bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    student_button.grid(row=2, column=0, padx=50, pady=20, sticky="nw")  # Added padx for spacing

    # Fee button (top right, below welcome message)
    fee_button = tk.Button(button_frame, text="Add Student",command=lambda: [dashboard.destroy(), add_students(root)], bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    fee_button.grid(row=1, column=1, padx=50, pady=20, sticky="ne")  # Added padx for spacing
'''
    # Room button (below fees)
    room_button = tk.Button(button_frame, text="Room", command=room_details, bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    room_button.grid(row=2, column=1, padx=50, pady=20, sticky="ne")  # Added padx for spacing

    # Laundry button (below student)
    laundry_button = tk.Button(button_frame, text="Laundry", command=laundry_management, bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    laundry_button.grid(row=3, column=0, padx=50, pady=20, sticky="nw")  # Added padx for spacing

    # Logout button (between Laundry and Hostel Gallery)
    logout_button = tk.Button(button_frame, text="Logout", command=logout, bg="#FF0000", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    logout_button.grid(row=3, column=1, padx=50, pady=20, sticky="ne")  # Added padx for spacing
'''

def meal_management(root):
    mealBoard = tk.Toplevel()
    mealBoard.title("Warden Sab")
    mealBoard.geometry("800x600")
    mealBoard.configure(bg="#f0f0f0")
    mealBoard.iconbitmap("abc.ico")

    # Welcome message
    welcome_label = tk.Label(mealBoard, text="Weekly Meal Plan", font=("Arial", 24, "bold"), bg="#F0F0F0", fg="black")
    welcome_label.pack(pady=20)

    # Connect to database
    conn = sqlite3.connect("data.db")  
    cursor = conn.cursor()

    # Fetch meal data
    cursor.execute("SELECT id, day, breakfast, meal, lunch, dinner FROM meal")
    meals = cursor.fetchall()
    conn.close()

    # Create table frame
    table_frame = tk.Frame(mealBoard, bg="#f0f0f0")
    table_frame.pack()

    # Table headers
    headers = ["Day", "Breakfast", "Meal", "Lunch", "Dinner"]
    for col, title in enumerate(headers):
        label = tk.Label(table_frame, text=title, font=("Arial", 14, "bold"), bg="lightgray", padx=10, pady=5, borderwidth=1, relief="solid")
        label.grid(row=0, column=col, sticky="nsew")

    # Dictionary to store entry widgets for updates
    entry_widgets = {}

    # Insert meal data into table with entry fields
    for row, meal in enumerate(meals, start=1):
        meal_id = meal[0]  # Store ID for updates
        entry_widgets[meal_id] = []

        for col, value in enumerate(meal[1:]):  # Skip ID column
            entry = tk.Entry(table_frame, font=("Arial", 12), bg="white", width=15)
            entry.insert(0, value)  # Pre-fill with existing data
            entry.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            entry_widgets[meal_id].append(entry)  # Store for later update

    # Function to save updates
    def save_changes():
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        for meal_id, entries in entry_widgets.items():
            updated_values = [entry.get() for entry in entries]  # Get updated values
            cursor.execute("""
                UPDATE meal 
                SET day = ?, breakfast = ?, meal = ?, lunch = ?, dinner = ? 
                WHERE id = ?
            """, (*updated_values, meal_id))

        conn.commit()
        conn.close()
        tk.messagebox.showinfo("Success", "Meal plan updated successfully!")

    # Save button
    save_button = tk.Button(mealBoard, text="Save Changes", font=("Arial", 14, "bold"), bg="green", fg="white", padx=10, pady=5, command=save_changes)
    save_button.pack(pady=20)

def students(rooot):
    mealBoard = tk.Toplevel()
    mealBoard.title("Students details")
    mealBoard.geometry("800x600")
    mealBoard.configure(bg="#f0f0f0")
    mealBoard.iconbitmap("abc.ico")

    # Welcome message
    welcome_label = tk.Label(mealBoard, text="Students details", font=("Arial", 24, "bold"), bg="#F0F0F0", fg="black")
    welcome_label.pack(pady=20)

def add_students(root):
    addStudent = tk.Toplevel(root)
    addStudent.title("Add Student")
    addStudent.geometry("800x600")
    addStudent.configure(bg="#f0f0f0")
    addStudent.iconbitmap("abc.ico")


    # Fetch available rooms
    def fetch_rooms():
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, floor, capacity, occupied FROM room WHERE occupied < capacity")
        rooms_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return rooms_list

    # Submit student and update room occupancy
    def submit():
        name = entries["Name"].get()
        dob = entries["Date of Birth (YYYY-MM-DD)"].get()
        address = entries["Address"].get()
        email = entries["Email"].get()
        number = entries["Phone Number"].get()
        parent_name = entries["Parent Name"].get()
        parent_number = entries["Parent Number"].get()
        entry_date = entries["Entry Date (YYYY-MM-DD)"].get()
        paid_till = entries["Paid Till (YYYY-MM-DD)"].get()
        selected_room = room_var.get()

        if not name or not dob or not address or not email or not number or not parent_name or not parent_number or not selected_room:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        room_number = int(selected_room.split()[1])  # Extract room ID from "Room X"

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        try:
            # Insert student into database
            cursor.execute("""
                INSERT INTO student (name, dob, address, email, number, parent_name, parent_number, entry_date, paid_till, room_number)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, dob, address, email, number, parent_name, parent_number, entry_date, paid_till, room_number))

            # Update room occupancy
            cursor.execute("UPDATE room SET occupied = occupied + 1 WHERE id = ?", (room_number,))

            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            admin_dashboard()
            addStudent.destroy()
            

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    # UI Elements
    tk.Label(addStudent, text="Add Student", font=("Arial", 24, "bold"), bg="#F0F0F0").pack(pady=20)

    labels = ["Name", "Date of Birth (YYYY-MM-DD)", "Address", "Email", "Phone Number",
              "Parent Name", "Parent Number", "Entry Date (YYYY-MM-DD)", "Paid Till (YYYY-MM-DD)"]
    entries = {}

    for label in labels:
        tk.Label(addStudent, text=label, font=("Arial", 12), bg="#F0F0F0").pack()
        entry = tk.Entry(addStudent, font=("Arial", 12))
        entry.pack(pady=2)
        entries[label] = entry

    # Room selection dropdown
    tk.Label(addStudent, text="Select Room", font=("Arial", 12), bg="#F0F0F0").pack()
    rooms = fetch_rooms()
    print(rooms)
    room_var = tk.StringVar()
    room_dropdown = ttk.Combobox(addStudent, textvariable=room_var, values=[f"Room {r[0]} (Floor {r[1]})" for r in rooms], state="readonly")
    room_dropdown.pack(pady=5)

    # Submit button
    tk.Button(addStudent, text="Submit", font=("Arial", 14), bg="#4CAF50", fg="white", command=submit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("abc.ico")
    login_page(root)
    root.mainloop()


