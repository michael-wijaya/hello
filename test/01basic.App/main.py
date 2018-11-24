from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!'
@app.route("/tuna")
def tuna():
    return '<h1>hello</h1>'
@app.route("/tuna/<username>")
def profile(username):
    return '<h1>hello there %s</h1>'%username
@app.route("/post/<int:post_id>")
def post(post_id):
    return '<h1>your post id is %s</h1>'%post_id
if __name__ == "__main__":
    app.run(debug=True)





















