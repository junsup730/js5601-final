
# import statements
from flask import Flask, render_template

# Flask app variable
app = Flask(__name__)


# static route
@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/1006")
def home1006():
    return render_template("home1006.html")


@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")


# start the server
if __name__ == "__main__":
    app.run()
