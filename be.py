from flask import Flask, request, jsonify, send_from_directory
import csv

app = Flask(__name__)

CSV_FILE = 'data.csv'

@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('.', path)

# Load CSV data
def load_csv():
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

# Save CSV data
def save_csv(data):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

@app.route('/get_csv', methods=['GET'])
def get_csv():
    data = load_csv()
    return jsonify(data)

@app.route('/save_csv', methods=['POST'])
def save_csv_data():
    data = request.get_json()
    save_csv(data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
