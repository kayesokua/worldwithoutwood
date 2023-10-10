import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('features.html', utc_dt=datetime.datetime.utcnow(), title="Title here")