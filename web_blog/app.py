from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_method():
    return "<h1><i>hello world<i><h1>"


if __name__ == "__main__":
    app.run(debug=True)
