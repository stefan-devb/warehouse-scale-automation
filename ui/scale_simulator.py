import tkinter as tk
from tkinter import messagebox
import json
import random
import requests


API_URL = "http://localhost:5001/upload"   # Backend endpoint


# ---- Simulation of scale sensor ----
def get_weight():
    """
    Simulates weight readings from a scale sensor.
    Generates a random float between 0.1 and 10.0 kg.
    """
    return round(random.uniform(0.1, 10.0), 2)


# ---- Sending data to backend ----
def send_data():
    color_code = color_entry.get().strip()
    weight = weight_label["text"]

    # Basic validation
    if not color_code or color_code == placeholder:
        messagebox.showwarning("Upozorenje", "Unesite kod boje!")
        return

    try:
        weight_value = float(weight)
    except ValueError:
        messagebox.showerror("Greška", "Neispravna težina!")
        return

    payload = {
        "color_code": color_code,
        "weight": weight_value
    }

    print("Šaljem JSON:", json.dumps(payload, indent=2))

    try:
        response = requests.post(API_URL, json=payload, timeout=3)
        if response.status_code == 200:
            messagebox.showinfo("Info", "Podaci poslani!")
        else:
            messagebox.showerror("Greška", f"Server vratio: {response.status_code}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Greška", f"Neuspjelo slanje: {e}")


# ---- Updating simulated scale reading ----
def update_weight():
    """
    Refreshes weight label every second with a new random weight.
    """
    weight = get_weight()
    weight_label.config(text=str(weight))
    root.after(1000, update_weight)


# ---- GUI ----
root = tk.Tk()
root.title("Scale Simulation UI")
root.geometry("300x200")

# Weight display
weight_label = tk.Label(root, text="0.0", font=("Helvetica", 24))
weight_label.pack(pady=20)

# Color code input
color_entry = tk.Entry(root, font=("Helvetica", 14))
color_entry.pack(pady=10)

placeholder = "Unesite kod boje"
color_entry.insert(0, placeholder)
color_entry.config(fg="grey")


def on_entry_click(event):
    if color_entry.get() == placeholder:
        color_entry.delete(0, "end")
        color_entry.config(fg="black")


def on_focusout(event):
    if color_entry.get().strip() == "":
        color_entry.insert(0, placeholder)
        color_entry.config(fg="grey")


color_entry.bind("<FocusIn>", on_entry_click)
color_entry.bind("<FocusOut>", on_focusout)

# Send button
send_button = tk.Button(root, text="Send", command=send_data)
send_button.pack(pady=10)

# Start periodic weight updates
update_weight()

# Start GUI loop
root.mainloop()

