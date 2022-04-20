from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('2022 SP.csv')
    return render_template('home.html', classes = df)

