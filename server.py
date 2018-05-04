from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "kwjehfi4uht"


@app.route("/")
def index():
    if 'count' not in session:
        session["number"] = random.randrange(1, 101)
        session["guess"] = 0
        session["count"] = 0

    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    session["guess"] = int(request.form["guessedNum"])
    session["count"] += 1

    return redirect("/")


@app.route("/reset")
def reset():
    session["count"] = 0
    session["number"] = random.randrange(1, 101)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)