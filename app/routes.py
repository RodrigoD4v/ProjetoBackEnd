# routes.py

import base64
from io import BytesIO
from flask import render_template, request, jsonify
from . import app
import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import traceback

def import_model():
    global modelo, encoder, scaler
    modelo_path = os.path.abspath('./data/models/logistic_regression.pkl')
    scaler_path = os.path.abspath('./data/models/scaler.pkl')
    modelo = pickle.load(open(modelo_path, 'rb'))
    scaler = pickle.load(open(scaler_path, 'rb'))
    return modelo, scaler

modelo, scaler = import_model()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all form data as a dictionary
        form_data = request.form.to_dict()

        # Convert relevant form data to int
        form_data['age'] = int(form_data['age'])
        form_data['balance'] = int(form_data['balance'])
        form_data['duration'] = int(form_data['duration'])
        form_data['campaign'] = int(form_data['campaign'])
        form_data['pdays'] = int(form_data['pdays'])
        form_data['previous'] = int(form_data['previous'])

        # Concatenate numerical data
        numerical_data = np.array([[form_data['age'], form_data['balance'], form_data['duration'], form_data['campaign'], form_data['pdays'], form_data['previous']]])
        parametros_scaled = scaler.transform(numerical_data)

        # Make the prediction
        resultado = modelo.predict(parametros_scaled)[0]
        
        if resultado == 'no':
            form_data['resultado_texto'] = 'Não há chances de subscrição'
        else:
            form_data['resultado_texto'] = 'Há chances de subscrição'

        return render_template('result.html', **form_data)
    
    except Exception as e:
        print(traceback.print_exc())
        return jsonify({'error': f'400 Bad Request: {str(e)}'}), 400

@app.route('/ecclientes', methods=['GET'])
def mostrarEcClientes():
    try:
        df = pd.read_csv('data/processed/bank_marketing_processed.csv')
        job_counts = df['job'].value_counts().to_dict()
        response = {
            'labels': list(job_counts.keys()),
            'values': list(job_counts.values())
        }
    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response)


@app.route('/educationclients', methods=['GET'])
def showEducationClients():
    try:
        df = pd.read_csv('data/processed/bank_marketing_processed.csv')
        education_counts = df['education'].value_counts().to_dict()
        response = {
            'labels': list(education_counts.keys()),
            'values': list(education_counts.values())
        }
    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response)


@app.route('/maritalstatusclients', methods=['GET'])
def showMaritalStatusClients():
    try: 
        df = pd.read_csv('data/processed/bank_marketing_processed.csv')
        marital_counts = df['marital'].value_counts().to_dict()
        response = {
            'labels': list(marital_counts.keys()),
            'values': list(marital_counts.values())
        }
    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response)

