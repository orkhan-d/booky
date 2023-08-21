from app import app

@app.route('/ping')
def ping():
    return {'result': 'pong'}

@app.route('/')
def home():
    return {'result': 'Hello World!'}