from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    # Za test: samo ispis u konzolu
    print("Primljeni podaci:", data)

    # Ovdje kasnije možeš pohraniti u SQLite / drugu bazu

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

