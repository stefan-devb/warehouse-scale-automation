import tkinter as tk
from tkinter import messagebox
import json
import random


# Funkcija koja simulira težinu sa vage
def get_weight():
    return round(random.uniform(0.1, 10.0), 2)  # težina između 1 i 10 kg


# Funkcija za slanje podataka
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

    # Za test, samo printamo JSON
    print("Šaljem JSON:", json.dumps(data))

    # Ovdje kasnije možeš dodati HTTP POST prema Flask API-u
    # requests.post("http://server_ip:port/endpoint", json=data)

    messagebox.showinfo("Info", "Podaci poslani!")


# Funkcija koja ažurira težinu na ekranu
def update_weight():
    weight = get_weight()
    weight_label.config(text=str(weight))
    root.after(1000, update_weight)  # ažurira svake sekunde


# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Warehouse Scale Tablet GUI")
root.geometry("300x200")

# Prikaz težine
weight_label = tk.Label(root, text="0.0", font=("Helvetica", 24))
weight_label.pack(pady=20)

# Polje za unos boje
color_entry = tk.Entry(root, font=("Helvetica", 14))
color_entry.pack(pady=10)

# Postavljanje placeholdera
placeholder = "Unesite kod boje"
color_entry.insert(0, placeholder)

# Funkcija koja briše placeholder kad se klikne u polje
def on_entry_click(event):
    if color_entry.get() == placeholder:
        color_entry.delete(0, "end")  # briše tekst
        color_entry.config(fg='black')  # opcionalno: promijeni boju teksta

# Funkcija koja vraća placeholder ako polje ostane prazno
def on_focusout(event):
    if color_entry.get() == '':
        color_entry.insert(0, placeholder)
        color_entry.config(fg='grey')

color_entry.bind("<FocusIn>", on_entry_click)
color_entry.bind("<FocusOut>", on_focusout)
color_entry.config(fg='grey')  # placeholder boja
# Dugme Send
send_button = tk.Button(root, text="Send", command=send_data)
send_button.pack(pady=10)

# Pokreće update težine
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
        response = requests.post("http://localhost:5000/upload", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Info", "Podaci poslani!")
        else:
            messagebox.showerror("Greška", f"Server vratio: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Greška", f"Neuspjelo slanje: {e}")

