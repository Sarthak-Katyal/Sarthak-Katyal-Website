from flask import Flask, request, render_template, send_from_directory
import pandas as pd
from json import load

app = Flask(__name__)

@app.route('/')
def foo():
    return render_template('index.html')

@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory("assets", path)