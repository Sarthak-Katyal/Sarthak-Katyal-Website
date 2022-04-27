from flask import Flask, request, render_template
import pandas as pd
from json import load

app = Flask(__name__)

@app.route('/')
def foo():
    # df = pd.read_csv('2022 SP.csv')
    return render_template('index.html')

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)