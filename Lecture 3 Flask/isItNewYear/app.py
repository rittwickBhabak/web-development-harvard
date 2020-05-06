from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    new_year = now.month == 1 and now.day == 1
    # new_year = "YES" if new_year==True else "NO"
    return render_template('index.html', new_year = new_year)