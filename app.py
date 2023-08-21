from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return {'result': 'pong'}

@app.route('/')
def home():
    return {'result': 'Hello World!'}