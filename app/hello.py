from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, K8S!</h1>"


def __main__():
    app.run(host='0.0.0.0', port='8000')
