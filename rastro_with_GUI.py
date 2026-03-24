import json
import os
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "reservations.json"

# Load data from file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        return {str(i): {} for i in range(1, 21)}

# Save data to file
def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(tables, f, indent=4)

tables = load_data()

def reserve_table():
    table = table_entry.get()
    name = name_entry.get()
    time = time_entry.get()

    if not table.isdigit() or int(table) not in range(1, 21):
        messagebox.showerror("Error", "Invalid table number")
        return

    if time in tables[table]:
        messagebox.showerror("Error", "Table already booked for this time")
    else:
        tables[table][time] = name
        save_data()
        tag = "VIP" if int(table) <= 5 else "Regular"
        messagebox.showinfo("Success", f"{tag} Table {table} booked for {name}")

def cancel_reservation():
    table = table_entry.get()
    time = time_entry.get()

    if table in tables and time in tables[table]:
        del tables[table][time]
        save_data()
        messagebox.showinfo("Cancelled", "Reservation cancelled")
    else:
        messagebox.showerror("Error", "No such booking")

def show_available():
    time = time_entry.get()
    available = []

    for t in tables:
        if time not in tables[t]:
            available.append(t)

    result = "Available Tables:\n" + ", ".join(available)
    messagebox.showinfo("Availability", result)

def show_all():
    result = ""

    for t in tables:
        if tables[t]:
            for time, name in tables[t].items():
                tag = "VIP" if int(t) <= 5 else "Regular"
                result += f"Table {t} ({tag}) | {time} | {name}\n"
        else:
            result += f"Table {t}: No bookings\n"

    messagebox.showinfo("All Reservations", result)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Restaurant Reservation System")
root.geometry("400x350")

tk.Label(root, text="Customer Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Table Number (1-20)").pack()
table_entry = tk.Entry(root)
table_entry.pack()

tk.Label(root, text="Time Slot (e.g. 7PM-9PM)").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root, text="Reserve Table", command=reserve_table).pack(pady=5)
tk.Button(root, text="Cancel Reservation", command=cancel_reservation).pack(pady=5)
tk.Button(root, text="Check Availability", command=show_available).pack(pady=5)
tk.Button(root, text="Show All Reservations", command=show_all).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
