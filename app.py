# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Deployed by Ahmed Khafagy - v4.0 - Kubernetes rolling update"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
