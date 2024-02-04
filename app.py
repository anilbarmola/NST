from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the Flask app"
@app.route("/index", methods=["GET"])
def index():
    return "<h1>Welcome to the index page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
