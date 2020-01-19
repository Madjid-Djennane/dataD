from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    a = {}
    a['mazigh'] = 'djennane'
    return a