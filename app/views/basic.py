from app import app
from flask import render_template

@app.route('/ping')
def ping():
    return {'result': 'pong'}

@app.route('/')
def home():
    return render_template('main.html')