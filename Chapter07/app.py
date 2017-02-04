__author__ = 'Chetan'

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

users = [
    {
        'id': 1,
        'username': u'cjgiridhar',
        'email': u'abc@xyz.com',
        'active': True
    },
    {
        'id': 2,
        'username': u'python',
        'email': u'py@py.org',
        'active': False
    }
]

@app.route('/v1/users/', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/v1/users/<int:id>/', methods=['GET'])
def get_user(id):
    for user in users:
        if user.get("id") == id:
            return jsonify({'users': user})
    abort(404)

@app.route('/v1/users/<int:id>/', methods=['PUT'])
def update_user(id):
    user = [user for user in users if user['id'] == id]
    user[0]['username'] = request.json.get('username', user[0]['username'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['active'] = request.json.get('active', user[0]['active'])
    return jsonify({'users': user[0]})

@app.route('/v1/users/<int:id>/', methods=['DELETE'])
def delete_user(id):
    user = [user for user in users if user['id'] == id]
    users.remove(user[0])
    return jsonify({}), 204

@app.route('/v1/users/', methods=['POST'])
def create_user():
    if not request.json or not 'email' in request.json:
        abort(404)
    user_id = users[-1].get("id") + 1
    username = request.json.get('username')
    email = request.json.get('email')
    status = False
    user = {"id": user_id, "email": email,
            "username": username, "active": status}
    users.append(user)
    return jsonify({'user':user}), 201

if __name__ == '__main__':
    app.run(debug=True)
