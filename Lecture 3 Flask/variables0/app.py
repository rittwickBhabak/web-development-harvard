from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello Rittwick!"
    return render_template('index.html',headline=headline)

@app.route("/<string:name>")
def morning_wish(name):
    headline = f"Good Morning, {name.capitalize()}"
    return render_template('index.html', headline=headline)

@app.route('/goodbye')
def bye():
    headline = "Good Bye!"
    return render_template('index.html', headline = headline)


