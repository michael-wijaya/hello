from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "the method is %s"%request.method
@app.route("/bacon",methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "you are using POST"
    else:
        return "you are probably using GET"


if __name__ == "__main__":
    app.run()