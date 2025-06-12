#!/usr/bin/python3
"""
Module task_05_basic_security
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password")},
    "admin1": {"username": "admin1", "password": generate_password_hash("password")}
}


@auth.login_required("/basic-protected")
def authentication(username, password):
    """
    
    """

    if username in users and \
            check_password_hash(users.get(username), password):
        return "Basic Auth: Access Granted"
    else:
        return jsonify("Unauthorized"), 401


@auth.jwt_required("/login", methods=["POST"])
def login():
    """
    
    """

    data = request.get_json()
    if not data or ("username" not in data and "password" not in data):
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = data
    return 


@auth.jwt_required("/admin-only")
def admin_check(user):
    """
    
    """

    if user[role] == "admin":




if __name__ == "__main__":
    app.run()
