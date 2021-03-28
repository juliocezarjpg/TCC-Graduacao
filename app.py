# rota heroku http://tcc-julio.herokuapp.com/
from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime


app = Flask(__name__)

dados = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/data_upload', methods=['POST'])
def data_upload():
    global dados
    json = request.get_json()
    dados.append(json)
    print(json)
    return '200'

@app.route('/api/v1/data_download', methods=['GET'])
def data_download():
    global dados
    data = dados.copy()
    dados.clear()
    return jsonify(data), '200'

@app.route('/api/v1/start', methods=['GET'])
def data_start():
    global dados
    dados.clear()
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return jsonify(timestamp), '200'
