from src.run_gh_file import run_gh_file
from flask import Flask, Blueprint



app = Flask(__name__)

@app.route("/")
def run_app():
    return "hello world!!!"

@app.route("/result/<input>")
def run_cal(input):
    return "result is {}".format(run_gh_file(int(input)))


if __name__ == "__main__":
    app.run(debug=False)
