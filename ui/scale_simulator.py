import tkinter as tk
from tkinter import messagebox
import json
import random


# Simulation of weight on scale
def get_weight():
    return round(random.uniform(0.1, 10.0), 2)  # težina između 1 i 10 kg


# Sending data to app
def send_data():
    color_code = color_entry.get()
    weight = weight_label['text']

    if not color_code:
        messagebox.showwarning("Upozorenje", "Unesite kod boje!")
        return

    data = {
        "Artikelnr.": color_code,
        "Menge": weight
    }

    # Za test, samo printamo JSON
    print("Šaljem JSON:", json.dumps(data))

    # Ovdje kasnije možeš dodati HTTP POST prema Flask API-u
    # requests.post("http://server_ip:port/endpoint", json=data)

    messagebox.showinfo("Info", "Podaci poslani!")


# Updates weight showed on screen
def update_weight():
    weight = get_weight()
    weight_label.config(text=str(weight))
    root.after(1000, update_weight)  # every second


# Main window
root = tk.Tk()
root.title("Scale Simulation UI")
root.geometry("300x200")

# Show weight in window
weight_label = tk.Label(root, text="0.0", font=("Helvetica", 24))
weight_label.pack(pady=20)

# Box for entering data
color_entry = tk.Entry(root, font=("Helvetica", 14))
color_entry.pack(pady=10)

# Text box placeholder
placeholder = "Unesite kod boje"
color_entry.insert(0, placeholder)

# Deleting placeholder when entering data
def on_entry_click(event):
    if color_entry.get() == placeholder:
        color_entry.delete(0, "end")  # deletes the text


# Showing placeholder back if no data entered
def on_focusout(event):
    if color_entry.get() == '':
        color_entry.insert(0, placeholder)
        color_entry.config(fg='grey')

color_entry.bind("<FocusIn>", on_entry_click)
color_entry.bind("<FocusOut>", on_focusout)
color_entry.config(fg='grey')  # placeholder color
# send button
send_button = tk.Button(root, text="Send", command=send_data)
send_button.pack(pady=10)

update_weight()

# Start GUI
root.mainloop()

import requests


def send_data():
    color_code = color_entry.get()
    weight = weight_label['text']

    if not color_code:
        messagebox.showwarning("Upozorenje", "Unesite kod boje!")
        return

    data = {
        "color_code": color_code,
        "weight": weight
    }

    try:
        response = requests.post("http://localhost:5001/upload", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Info", "Podaci poslani!")
        else:
            messagebox.showerror("Greška", f"Server vratio: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Greška", f"Neuspjelo slanje: {e}")

