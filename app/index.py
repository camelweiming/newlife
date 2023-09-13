from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def work():
    return "<p>Hello, World!</p>"