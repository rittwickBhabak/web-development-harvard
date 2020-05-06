from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=["POST"])
def hello():
    name = request.form.get('name').capitalize()
    return render_template('hello.html', name=name)


@app.route('/hi',methods=["POST", "GET"])
def hi():
    if(request.method=="GET"):
        return "Please submit the form instead"
    else:
        name = request.form.get('name').capitalize()
        return render_template('hello.html', name=name)