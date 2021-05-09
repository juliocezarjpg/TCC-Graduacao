# rota heroku http://tcc-julio.herokuapp.com/
from flask import Flask, render_template, url_for, request, jsonify, g
from datetime import datetime
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

DATABASE = 'database/database.db'

dados = []

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def set_status(status):
    db = get_db()
    cur = db.cursor()
    cur.execute(f'UPDATE status SET status = {status}  where id = 1')
    db.commit()

def get_status():
    db = get_db()
    cur = db.cursor()
    status = list(cur.execute('SELECT status FROM status WHERE id = 1'))
    return status[0][0]

def set_image(image):
    db = get_db()
    cur = db.cursor()
    cur.execute(f'UPDATE stream SET stream = {image}  where id = 1')
    db.commit()

def get_image():
    db = get_db()
    cur = db.cursor()
    image = list(cur.execute('SELECT stream FROM stream WHERE id = 1'))
    return image[0][0]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/data_upload', methods=['POST'])
def data_upload():
    global dados
    json = request.get_json()
    now = datetime.now()
    json['timestamp']  = datetime.timestamp(now)
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
    set_status(1)   
    dados.clear()
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return jsonify(timestamp), '200'

@app.route('/api/v1/end', methods=['POST'])
def data_end():
    global dados
    set_status(3)
    dados.clear()
    return '200'

@app.route('/api/v1/status', methods=['GET'])
def data_status():
    return str(get_status()), '200'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/api/v1/img_upload', methods=['POST'])
def img_upload():
    json = request.get_json()
    img = str(json)
    #set_image(img)
    return img, '200'

@app.route('/api/v1/img_download', methods=['GET'])
def img_download():
    #global img
    return jsonify(get_image()), '200'