from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def data():
    return jsonify(list(users.keys()))  # Return list of usernames

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    
    # Check for required fields
    if not user_data or 'username' not in user_data or 'name' not in user_data:
        return jsonify({"error": "Username and name are required."}), 400
    
    username = user_data['username']
    
    # Check for duplicate username
    if username in users:
        return jsonify({"error": "User already exists."}), 400
    
    users[username] = {
        "username": username,
        "name": user_data['name'],
        "age": user_data.get('age', None),  # Optional
        "city": user_data.get('city', None)  # Optional
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/status', methods=['GET'])
def status():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
