from flask import Flask, request, jsonify

app = Flask(__name__)
data = []  # This will store our data

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify({"message": "Data added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
