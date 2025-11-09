from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "warehouse_ham_data.db"

# Table creation
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            color_code TEXT NOT NULL,
            weight REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Saves received data to DB
def save_to_db(color_code, weight):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weights (color_code, weight, timestamp)
        VALUES (?, ?, ?)
    ''', (color_code, weight, datetime.now().isoformat()))
    conn.commit()
    conn.close()

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    color_code = data.get("color_code")
    weight = float(data.get("weight"))

    if not color_code or weight is None:
        return jsonify({"error": "Invalid data"}), 400

    save_to_db(color_code, weight)
    print(f"Podaci spremljeni: {color_code}, {weight} kg")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
