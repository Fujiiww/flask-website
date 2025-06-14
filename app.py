from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")

if "__main__" == __name__:
    app.run(debug=True)