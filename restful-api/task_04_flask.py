#!/usr/bin/python3
"""
Module task_04_flask
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

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
    return jsonify({"username" : username})


@app.route("/status")
def status():
    """
    Handle root URL "/status"
    """

    return "OK"

@app.route("/users/<username>")
def username(username):
    """
    Handle root URL "/users/<username>"
    """
    try:
        return jsonify({"username" : username})
    except Exception as e:
        return {"error": "User not found"}


@app.route("/add_user")
def add_user():
    """
    Handle root URL "/add_user"
    """

    with app.test_request_context('/add_user', method='POST'):
        assert request.path == '/add_user'
        assert request.method == 'POST'
        assert request.status_code == '201'

if __name__ == "__main__": app.run()