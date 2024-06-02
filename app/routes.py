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
    df = pd.read_csv('data/processed/bank_marketing_processed.csv')
            
    job_counts = df['job'].value_counts()

     # Convertendo os dados para um formato JSON
    data = {
         'labels': job_counts.index.tolist(),
           'values': job_counts.values.tolist()
        }

    return jsonify(data)

@app.route('/maritalstatusclients', methods=['GET'])
def showMaritalStatusClients():
        df = pd.read_csv('data/processed/bank_marketing_processed.csv')
            
        marital_counts = df['marital'].value_counts()

        # Convertendo os dados para um formato JSON
        data = {
            'labels': marital_counts.index.tolist(),
            'values': marital_counts.values.tolist()
        }

        return jsonify(data)

@app.route('/educationclients', methods=['GET'])
def showEducationClients():
        df = pd.read_csv('data/processed/bank_marketing_processed.csv')
            
        education_counts = df['education'].value_counts()

        # Convertendo os dados para um formato JSON
        data = {
            'labels': education_counts.index.tolist(),
            'values': education_counts.values.tolist()
        }

        return jsonify(data)
    
    