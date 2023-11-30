from flask import request, jsonify, render_template
from app import app
from app.auth import check_auth_token
from hashlib import sha1

# In-memory storage for user data, segregated by tenant
users = {}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/v1/user", methods=['POST'])
def create_user():
    valid, tenant_id = check_auth_token()
    if not valid:
        return jsonify({'users': [], 'errors': ['Invalid Auth Token']}), 401

    if tenant_id not in users:
        users[tenant_id] = {}

    data = request.get_json()
    username = data['username']
    password = data['password']
    user_id = len(users[tenant_id]) + 1
    password_hash = sha1(f"{username}{password}".encode()).hexdigest()
    users[tenant_id][user_id] = {'username': username, 'password': password_hash}

    return jsonify({'users': [{'user_id': user_id, 'username': username, 'password': password_hash}], 'errors': []}), 201

@app.route('/v1/user', methods=['GET'])
def get_user():
    valid, tenant_id = check_auth_token()
    if not valid:
        return jsonify({'users': [], 'errors': ['Unauthorized']}), 401

    if tenant_id not in users:
        return jsonify({'users': [], 'errors': ['No users for this tenant']}), 404

    user_id = request.args.get('user_id', type=int)
    if user_id:
        user = users[tenant_id].get(user_id)
        if user:
            return jsonify({'users': [{'user_id': user_id, **user}], 'errors': []}), 200
        else:
            return jsonify({'users': [], 'errors': ['User not found']}), 404
    else:
        all_users = [{'user_id': uid, **data} for uid, data in users[tenant_id].items()]
        return jsonify({'users': all_users, 'errors': []}), 200

@app.route('/v1/user', methods=['PUT'])
def update_user():
    valid, tenant_id = check_auth_token()
    if not valid:
        return jsonify({'users': [], 'errors': ['Unauthorized']}), 401

    if tenant_id not in users:
        return jsonify({'users': [], 'errors': ['No users for this tenant']}), 404

    user_id = request.args.get('user_id', type=int)
    data = request.get_json()
    if user_id and user_id in users[tenant_id] and data:
        username = data.get('username')
        password = data.get('password')
        password_hash = sha1(f"{username}{password}".encode()).hexdigest()
        users[tenant_id][user_id] = {'username': username, 'password': password_hash}
        return jsonify({'users': [{'user_id': user_id, 'username': username, 'password': password_hash}], 'errors': []}), 200
    else:
        return jsonify({'users': [], 'errors': ['User not found or invalid data']}), 404

@app.route('/v1/user', methods=['DELETE'])
def delete_user():
    valid, tenant_id = check_auth_token()
    if not valid:
        return jsonify({'users': [], 'errors': ['Unauthorized']}), 401

    if tenant_id not in users:
        return jsonify({'users': [], 'errors': ['No users for this tenant']}), 404

    user_id = request.args.get('user_id', type=int)
    if user_id and user_id in users[tenant_id]:
        del users[tenant_id][user_id]
        return jsonify({'users': [], 'errors': []}), 200
    else:
        return jsonify({'users': [], 'errors': ['User not found']}), 404
