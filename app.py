from src.run_gh_file import gh_addition
from src.run_gh_file import gh_make_sphere
from flask import Flask



app = Flask(__name__)

@app.route("/")
def run_app():
    return "hello world!!!"

@app.route("/result/<num1>/<num2>")
def run_cal(num1, num2):
    return "result is {}".format(gh_addition(int(num1) + int(num2)))

@app.route("/makeSphere/<radius>")
def run_make_sphere(radius):
    print(radius)
    return gh_make_sphere(float(radius))

if __name__ == "__main__":
    app.run(debug=True)
