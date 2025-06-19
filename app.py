from flask import Flask, jsonify, send_from_directory, request
import random

app = Flask(__name__, static_folder='static')

# Start with an empty list of participants
participants = []

@app.route('/api/add', methods=['POST'])
def add_participant():
    data = request.get_json()
    name = data.get('name', '').strip()

    if not name:
        return jsonify({'error': 'Name cannot be empty'}), 400

    participants.append(name)
    return jsonify({'message': f'{name} has been added!'})

@app.route('/api/draw')
def draw_winner():
    if not participants:
        return jsonify({"error": "No participants left."}), 400
    winner = random.choice(participants)
    return jsonify({"winner": winner})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    print("🎯 Flask server running...")
    app.run(debug=True)
