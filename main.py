from flask import Flask, request

app = Flask(__name__)

@app.route("/api")
def main():
    return "DEPLYMENT"

@app.route("/")
def home():
    return "HOME PAGE"
if __name__ == "__main__":
    app.run(debug=True)