from flask import Flask, request, render_template
import pandas as pd
from json import load

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('2022 SP.csv')
    return render_template('home.html', classes = df)

