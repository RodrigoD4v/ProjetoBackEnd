from flask import render_template, request, jsonify
from . import app
import os
import pickle
import numpy as np


def import_model():
  modelo_path = os.path.abspath('./data/models/logistic_regression.pkl')
  scaler_path = os.path.abspath('./data/models/scaler.pkl')
  modelo = pickle.load(open(modelo_path, 'rb'))
  scaler = pickle.load(open(scaler_path, 'rb'))
  return modelo, encoder, scaler

modelo, encoder, scaler = import_model()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        balance = float(request.form['balance'])
        duration = float(request.form['duration'])
        campaign = float(request.form['campaign'])
        pdays = float(request.form['pdays'])
        previous = float(request.form['previous'])

        numerical_data = np.array([[age, balance, duration, campaign, pdays, previous]])
        parametros_scaled = scaler.transform(numerical_data)

        resultado = modelo.predict(parametros_scaled)[0]

        if resultado == 'no':
            resultado_texto = 'Não há chances de subscrição'
        else:
            resultado_texto = 'Há chances de subscrição'

        return f'Seu resultado é: "{resultado_texto}"!'
    except Exception as e:
        return jsonify({'error': f'400 Bad Request: {str(e)}'}), 400