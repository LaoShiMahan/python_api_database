import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])

def home():
    return (
        """
            <h1>This is our API</h1>
        """
    )

@app.route("/api/all", methods=["GET"])

def api_all():
    connection = sqlite3.connect("../database.db")
    records = connection.execute(
        """
            SELECT *
            FROM EMPLOYEES
        """
    ).fetchall()

    return jsonify(records)

@app.errorhandler(404)

def not_found(e):
    return (
        """
            <h1>{}</h1>
        """
        .format(e)
    )

app.run()