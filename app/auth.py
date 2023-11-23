from flask import Flask, request, jsonify
from hashlib import sha1
from app import app

# Configuration
from config import AUTH_TOKEN

def check_auth_token():
    token = request.headers.get('Authorization')
    return token == f"Bearer {AUTH_TOKEN}"