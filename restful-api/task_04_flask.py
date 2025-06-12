#!/usr/bin/python3
"""
Module task_04_flask
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    Handle root URL "/"
    """

    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Handle root URL "/data"
    """

    return jsonify(list(users.keys())), 200


@app.route("/status")
def status():
    """
    Handle root URL "/status"
    """

    return "OK"


@app.route("/users/<username>")
def username_route(username):
    """
    Handle root URL "/users/<username>"
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 400


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handle root URL "/add_user"
    """

    data = request.get_json()
    print("Reçu :", data)
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
