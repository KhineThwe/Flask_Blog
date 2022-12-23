from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return "<p>About Page!</p>"

if __name__ == '__main__':
    app.run(debug=True)
    #ဒါရေးပြီးရင် ဒီလို run လို့ရ python flask_blog.py