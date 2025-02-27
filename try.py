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
    fee_button = tk.Button(button_frame, text="Add Student", command=lambda: [dashboard.destroy(), add_students(root)], bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    fee_button.grid(row=1, column=1, padx=50, pady=20, sticky="ne")  # Added padx for spacing

    # New Room Details Button (below Add Student)
    room_button = tk.Button(button_frame, text="Room Details", command=lambda: [dashboard.destroy(), room()], bg="#4CAF50", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    room_button.grid(row=2, column=1, padx=50, pady=20, sticky="ne")  # Added padx for spacing

    # Logout button (bottom right corner, below Room Details)
    logout_button = tk.Button(button_frame, text="Logout", command=lambda: [dashboard.destroy(), login_page(root)], bg="#FF0000", fg="white", font=("Arial", 14), width=button_width, height=button_height)
    logout_button.grid(row=3, column=1, padx=50, pady=20, sticky="se")  # Added padx for spacing


def meal_management(root):
    mealBoard = tk.Toplevel()
    mealBoard.title("Warden Sab")
    mealBoard.geometry("800x600")
    mealBoard.configure(bg="#f0f0f0")
    mealBoard.iconbitmap("abc.ico")
        # Set the window to full screen
    mealBoard.attributes('-fullscreen', True)

    # Add a small arrow button at the top-left corner
    back_button = tk.Label(mealBoard, text="←", font=("Arial", 10), bg="#f0f0f0", fg="black", cursor="hand2")
    back_button.place(x=10, y=10)  # Position at the top-left corner
    back_button.bind("<Button-1>", lambda e: [mealBoard.destroy(), admin_dashboard()]) 

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

def students(root):
    students_win = tk.Toplevel(root)
    students_win.title("Students Details")
    students_win.geometry("1000x600")
    students_win.configure(bg="#f0f0f0")
    students_win.iconbitmap("abc.ico")

    # Set the window to full screen
    students_win.attributes('-fullscreen', True)

    # Add a small arrow button at the top-left corner
    back_button = tk.Label(students_win, text="←", font=("Arial", 10), bg="#f0f0f0", fg="black", cursor="hand2")
    back_button.place(x=10, y=10)  # Position at the top-left corner
    back_button.bind("<Button-1>", lambda e: [students_win.destroy(), admin_dashboard()])  # Bind click event

    # Welcome message
    welcome_label = tk.Label(students_win, text="Students Details", font=("Arial", 24, "bold"), bg="#F0F0F0", fg="black")
    welcome_label.pack(pady=20)

    # Create a frame for the search bar
    search_frame = tk.Frame(students_win, bg="#f0f0f0")
    search_frame.pack(fill="x", padx=20, pady=10)

    # Search bar components
    tk.Label(search_frame, text="Search:", font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=5)
    search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
    search_entry.pack(side="left", padx=5)
    search_button = tk.Button(search_frame, text="Search", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: search_students())
    search_button.pack(side="left", padx=5)

    # Create a frame for the table
    table_frame = tk.Frame(students_win, bg="#f0f0f0")
    table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Create a Treeview widget
    columns = ("ID", "Name", "DOB", "Address", "Email", "Phone", "Parent Name", "Parent Phone", "Entry Date", "Paid Till", "Room Number")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
    tree.pack(fill="both", expand=True)

    # Define column headings
    for col in columns:
        tree.heading(col, text=col)

    # Define column widths
    tree.column("ID", width=50)
    tree.column("Name", width=150)
    tree.column("DOB", width=100)
    tree.column("Address", width=200)
    tree.column("Email", width=150)
    tree.column("Phone", width=100)
    tree.column("Parent Name", width=150)
    tree.column("Parent Phone", width=100)
    tree.column("Entry Date", width=100)
    tree.column("Paid Till", width=100)
    tree.column("Room Number", width=100)

    # Function to load all student data into the table
    def load_students():
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()
        conn.close()

        # Clear existing data in the table
        for row in tree.get_children():
            tree.delete(row)

        # Insert all data into the table
        for student in students:
            tree.insert("", "end", values=student)

    # Function to search and highlight student data
    def search_students():
        search_term = search_entry.get().strip().lower()
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()
        conn.close()

        # Clear existing data in the table
        for row in tree.get_children():
            tree.delete(row)

        # Insert filtered and highlighted data
        for student in students:
            # Check if search term matches any field (case-insensitive)
            if search_term and any(search_term in str(field).lower() for field in student):
                # Highlight matching rows with a tag
                tree.insert("", "end", values=student, tags=("highlight",))
            elif not search_term:
                # If search term is empty, show all students without highlighting
                tree.insert("", "end", values=student)

        # Configure the highlight tag
        tree.tag_configure("highlight", background="yellow")

    # Function to edit a student record
    def edit_student():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to edit!")
            return

        # Get the selected student's data
        student_data = tree.item(selected_item, "values")

        # Create a new window for editing
        edit_win = tk.Toplevel(students_win)
        edit_win.title("Edit Student")
        edit_win.geometry("400x500")
        edit_win.configure(bg="#f0f0f0")

        # Create entry fields for editing
        entries = {}
        labels = ["ID", "Name", "DOB", "Address", "Email", "Phone", "Parent Name", "Parent Phone", "Entry Date", "Paid Till", "Room Number"]
        for i, label in enumerate(labels):
            tk.Label(edit_win, text=label, font=("Arial", 12), bg="#F0F0F0").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            if label == "ID":
                # Make ID read-only
                entry = tk.Entry(edit_win, font=("Arial", 12), state="readonly")
            else:
                entry = tk.Entry(edit_win, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            entry.insert(0, student_data[i])
            entries[label] = entry

        # Function to save the edited data
        def save_edit():
            updated_data = [entries[label].get() for label in labels]
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE student 
                SET name=?, dob=?, address=?, email=?, number=?, parent_name=?, parent_number=?, entry_date=?, paid_till=?, room_number=?
                WHERE id=?
            """, (*updated_data[1:], updated_data[0]))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student record updated successfully!")
            edit_win.destroy()
            load_students()  # Reload all students after edit

        # Save button
        tk.Button(edit_win, text="Save", font=("Arial", 14), bg="#4CAF50", fg="white", command=save_edit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Function to remove a student record
    def remove_student():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to remove!")
            return

        # Get the selected student's ID
        student_id = tree.item(selected_item, "values")[0]

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")
        if not confirm:
            return

        # Delete the student from the database
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()

        # Remove the student from the table
        tree.delete(selected_item)
        messagebox.showinfo("Success", "Student removed successfully!")

    # Load initial student data into the table
    load_students()

    # Add buttons for editing and removing students
    button_frame = tk.Frame(students_win, bg="#f0f0f0")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Edit Selected Student", font=("Arial", 14), bg="#4CAF50", fg="white", command=edit_student).pack(side="left", padx=10)
    tk.Button(button_frame, text="Remove Selected Student", font=("Arial", 14), bg="#FF0000", fg="white", command=remove_student).pack(side="left", padx=10)
def add_students(root):
    addStudent = tk.Toplevel(root)
    addStudent.title("Add Student")
    addStudent.geometry("800x600")
    addStudent.configure(bg="#f0f0f0")
    addStudent.iconbitmap("abc.ico")

    # Set the window to full screen
    addStudent.attributes('-fullscreen', True)

    # Add a small arrow button at the top-left corner
    back_button = tk.Label(addStudent, text="←", font=("Arial", 10), bg="#f0f0f0", fg="black", cursor="hand2")
    back_button.place(x=10, y=10)  # Position at the top-left corner
    back_button.bind("<Button-1>", lambda e: [addStudent.destroy(), admin_dashboard()])  # Bind click event

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
def room():
    room_win = tk.Toplevel()
    room_win.title("Room Details")
    room_win.geometry("1000x600")
    room_win.configure(bg="#f0f0f0")
    room_win.iconbitmap("abc.ico")
    room_win.attributes('-fullscreen', True)

    # Add a small arrow button at the top-left corner
    back_button = tk.Label(room_win, text="←", font=("Arial", 10), bg="#f0f0f0", fg="black", cursor="hand2")
    back_button.place(x=10, y=10)  # Position at the top-left corner
    back_button.bind("<Button-1>", lambda e: [room_win.destroy(), admin_dashboard()])  # Bind click event

    # Welcome message
    welcome_label = tk.Label(room_win, text="Room Details", font=("Arial", 24, "bold"), bg="#F0F0F0", fg="black")
    welcome_label.pack(pady=20)

    # Create a frame for the table
    table_frame = tk.Frame(room_win, bg="#f0f0f0")
    table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Create a Treeview widget
    columns = ("Room ID", "Floor", "Capacity", "Occupied", "Beds Left", "Students")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
    tree.pack(fill="both", expand=True)

    # Define column headings
    for col in columns:
        tree.heading(col, text=col)

    # Define column widths
    tree.column("Room ID", width=100)
    tree.column("Floor", width=100)
    tree.column("Capacity", width=100)
    tree.column("Occupied", width=100)
    tree.column("Beds Left", width=100)
    tree.column("Students", width=300)

    # Function to load room data into the table
    def load_rooms():
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        # Fetch room data
        cursor.execute("SELECT id, floor, capacity, occupied FROM room")
        rooms = cursor.fetchall()

        for room_data in rooms:
            room_id, floor, capacity, occupied = room_data
            beds_left = capacity - occupied

            # Fetch students in the room
            cursor.execute("SELECT name FROM student WHERE room_number = ?", (room_id,))
            students = cursor.fetchall()
            student_names = ", ".join([student[0] for student in students])

            # Insert data into the table
            tree.insert("", "end", values=(room_id, floor, capacity, occupied, beds_left, student_names))

        conn.close()

    # Load room data into the table
    load_rooms()

    # Function to edit room details
    def edit_room():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to edit!")
            return

        # Get the selected room's data
        room_data = tree.item(selected_item, "values")

        # Create a new window for editing
        edit_win = tk.Toplevel(room_win)
        edit_win.title("Edit Room Details")
        edit_win.geometry("400x300")
        edit_win.configure(bg="#f0f0f0")

        # Labels and entry fields for editing
        labels = ["Room ID", "Floor", "Capacity", "Occupied"]
        entries = {}

        for i, label in enumerate(labels):
            tk.Label(edit_win, text=label, font=("Arial", 12), bg="#F0F0F0").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(edit_win, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            entry.insert(0, room_data[i])  # Pre-fill with existing data
            entries[label] = entry

        # Function to save the edited room details
        def save_edit():
            updated_data = [entries[label].get() for label in labels]
            room_id = updated_data[0]  # Room ID is not editable, used for WHERE clause

            # Validate capacity and occupied values
            try:
                capacity = int(updated_data[2])
                occupied = int(updated_data[3])
                if capacity < occupied:
                    messagebox.showerror("Error", "Capacity cannot be less than occupied beds!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Capacity and Occupied must be integers!")
                return

            # Update the room in the database
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE room 
                SET floor = ?, capacity = ?, occupied = ?
                WHERE id = ?
            """, (updated_data[1], capacity, occupied, room_id))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Room details updated successfully!")
            edit_win.destroy()
            tree.delete(*tree.get_children())  # Clear the table
            load_rooms()  # Reload the table with updated data

        # Save button
        tk.Button(edit_win, text="Save", font=("Arial", 14), bg="#4CAF50", fg="white", command=save_edit).grid(row=len(labels), column=0, columnspan=2, pady=10)

   
     

    # Add buttons for editing and removing rooms
    button_frame = tk.Frame(room_win, bg="#f0f0f0")
    button_frame.pack(pady=10)

    edit_button = tk.Button(button_frame, text="Edit Selected Room", font=("Arial", 14), bg="#4CAF50", fg="white", command=edit_room)
    edit_button.pack(side="left", padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("abc.ico")
    login_page(root)
    root.mainloop()
