from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the DevOps app - develop version"

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/about")
def about():
    return jsonify({"app": "devops-app", "author": "Your Name"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
