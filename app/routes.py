from flask import Flask, request, jsonify, render_template
from app import app
from app.auth import check_auth_token
from hashlib import sha1

# In-memory storage for user data
users = {}

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/v1/user", methods=['POST'])
def create_user():
    if not check_auth_token():
        return jsonify({'users':[], 'errors':['Invalid Auth Token']}), 401
    
    data = request.get_json()
    username = data['username']
    password = data['password']
    user_id = len(users) + 1
    password_hash = sha1(f"{username}{password}".encode()).hexdigest()
    users[user_id] = {'username': username, 'password': password_hash}

    return jsonify({'users': [{'user_id': user_id, 'username': username, 'password': password_hash}], 'errors': []}), 201

@app.route('/v1/user', methods=['GET'])
def get_user():
    if not check_auth_token():
        return jsonify({'users': [], 'errors': ['Unauthorized']}), 401

    user_id = request.args.get('user_id', type=int)
    if user_id:
        user = users.get(user_id)
        if user:
            return jsonify({'users': [{'user_id': user_id, **user}], 'errors': []}), 200
        else:
            return jsonify({'users': [], 'errors': ['User not found']}), 404
    else:
        all_users = [{'user_id': uid, **data} for uid, data in users.items()]
        return jsonify({'users': all_users, 'errors': []}), 200

@app.route('/v1/user', methods=['PUT'])
def update_user():
    if not check_auth_token():
        return jsonify({'users': [], 'errors': ['Unauthorized']}), 401

    user_id = request.args.get('user_id', type=int)
    data = request.get_json()
    if user_id in users and data:
        username = data.get('username')
        password = data.get('password')
        password_hash = sha1(f"{username}{password}".encode()).hexdigest()
        users[user_id] = {'username': username, 'password': password_hash}
        return jsonify({'users': [{'user_id': user_id, 'username': username, 'password': password_hash}], 'errors': []}), 200
    else:
        return jsonify({'users': [], 'errors': ['User not found or invalid data']}), 404

@app.route('/v1/user', methods=['DELETE'])
def delete_user():
    if not check_auth_token():
        return jsonify({'users': [], 'errors': ['Unauthorized']}), 401

    user_id = request.args.get('user_id', type=int)
    if user_id in users:
        del users[user_id]
        return jsonify({'users': [], 'errors': []}), 200
    else:
        return jsonify({'users': [], 'errors': ['User not found']}), 404
