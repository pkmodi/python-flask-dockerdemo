from flask import flask

app = flask (__name__)

@app.route("/")
def hello_world():
    return 'cst Docker 101'