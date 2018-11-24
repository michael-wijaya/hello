from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html",user=user)


@app.route("/profile/<name>")
def hello(name):
    return render_template('profile.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)