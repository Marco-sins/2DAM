from flask import Flask, jsonify

app = Flask(__name__)

users = {
    "1": {"name": "Alice", "age": 30},
    "2": {"name": "Bob", "age": 25},
    "3": {"name": "Charlie", "age": 35}
}

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
if __name__ == '__main__':
    app.run(port=5001, debug=True)