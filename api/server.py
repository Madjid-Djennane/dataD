from flask import Flask
from datetime import datetime
from flask import jsonify
from index import *

# flask app
app = Flask(__name__)

# initialisation de la variable data
data = getDT('access2.log')

# 
@app.route('/', methods=['GET'])
def hello_world():
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    

# Retourne les hits http selon une fenêtre de temps
@app.route('/trafic/<date1>/<date2>', methods=['GET'])
def trafic(date1,date2):
    temp = getHttpHits(data, date1,date2).to_json(orient='values')
    response = jsonify(temp)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Retourne les ip triées par ordre décroissant
@app.route('/ips', methods=['GET'])
def ips():
    temp = getIps(data).to_json(orient='values')
    response = jsonify(temp)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response