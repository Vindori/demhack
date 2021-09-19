from flask import Flask, request, jsonify, send_from_directory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

import pickle
import numpy as np
import os

AI_PATH = os.path.join(os.getcwd(), '../model/')


app = Flask(__name__)

@app.route('/api/get_score/', methods=['POST'])
def get_score():
    text = request.form.get('text')

    vect = pickle.load(open(os.path.join(AI_PATH, 'tfidf.pickle'), 'rb'))
    loaded_model = pickle.load(open(os.path.join(AI_PATH, 'finalized_model.sav'), 'rb'))

    text = vect.transform([text])
    prediction = loaded_model.predict_proba(text)

    score = round(prediction[0][1] * 10000) / 100

    if score > 50:
        score = (score + 100) / 2
    else:
        score = score / 2

    response = jsonify(score=score)
    response.headers.add("Access-Control-Allow-Origin", "*")    

    return response\

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('front/js', path)

@app.route('/style.css')
def send_css():
    return send_from_directory('front/', 'style.css')

@app.route('/')
def index():
    return send_from_directory('front/', 'index.html')

app.run(host='localhost', port=8080, debug=True)
