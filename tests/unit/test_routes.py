import unittest
from app.routes import import_model, predict, mostrarEcClientes, showMaritalStatusClients, showEducationClients
from flask import Flask, request
import os
from unittest.mock import patch
import pandas as pd

class TestImportModel(unittest.TestCase):
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()
        self.app.route('/predict', methods=['POST'])(predict)
        self.app.route('/ecclientes', methods=['GET'])(mostrarEcClientes)
        self.app.route('/maritalstatusclients', methods=['GET'])(showMaritalStatusClients)
        self.app.route('/educationclients', methods=['GET'])(showEducationClients)

    def test_import_model(self):
        # Cenário 1: Testa se o modelo e o scaler foram importados corretamente
        modelo, scaler = import_model()
        self.assertIsNotNone(modelo)
        self.assertIsNotNone(scaler)
        print("Cenário 1: Modelo e scaler importados com sucesso.")

    @patch('app.routes.render_template')
    def test_predict_no_chances(self, mock_render_template):
        # Cenário 1: Testa se a resposta é correta quando não há chances de subscrição
        mock_render_template.return_value = 'Não há chances de subscrição'
        with self.app.test_request_context('/predict', method='POST', data={
            'age': 30,
            'balance': 1000,
            'duration': 100,
            'campaign': 1,
            'pdays': 5,
            'previous': 0
        }):
            response = predict()
            self.assertIn('Não há chances de subscrição', response)
            print("Cenário 1: Resposta para 'Não há chances de subscrição':", response)

        # Cenário 2: Testa se a resposta é correta quando há chances de subscrição
        mock_render_template.return_value = 'Há chances de subscrição'
        with self.app.test_request_context('/predict', method='POST', data={
            'age': 40,
            'balance': 2000,
            'duration': 150,
            'campaign': 2,
            'pdays': 10,
            'previous': 1
        }):
            response = predict()
            self.assertIn('Há chances de subscrição', response)
            print("Cenário 2: Resposta para 'Há chances de subscrição':", response)

        # Cenário 3: Testa se a resposta é correta quando os dados enviados são inválidos
        with self.app.test_request_context('/predict', method='POST', data={
            'age': 'invalid',
            'balance': 2000,
            'duration': 150,
            'campaign': 2,
            'pdays': 10,
            'previous': 1
        }):
            response, status_code = predict()
            self.assertEqual(status_code, 400)
            self.assertIn('400 Bad Request', response.json['error'])
            print("Cenário 3: Resposta para dados inválidos:", response.json)

    @patch('pandas.read_csv')
    def test_mostrarEcClientes(self, mock_read_csv):
        # Cenário 1: Testa se a resposta é correta quando há dados válidos
        mock_read_csv.return_value = pd.DataFrame({
            'job': ['admin.', 'blue-collar', 'technician', 'admin.', 'blue-collar']
        })
        response = self.client.get('/ecclientes')
        self.assertEqual(response.status_code, 200)
        self.assertIn('admin.', response.json['labels'])
        print("Cenário 1: Resposta com dados válidos para /ecclientes:", response.json)

        # Cenário 2: Testa se a resposta é correta quando não há dados
        mock_read_csv.return_value = pd.DataFrame({'job': []})
        response = self.client.get('/ecclientes')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['labels'], [])
        print("Cenário 2: Resposta sem dados para /ecclientes:", response.json)

        # Cenário 3: Testa se a resposta é correta quando há um erro na leitura do CSV
        mock_read_csv.side_effect = Exception("Error reading CSV")
        response = self.client.get('/ecclientes')
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], "Error reading CSV")
        print("Cenário 3: Resposta com erro na leitura do CSV:", response.json)

    @patch('pandas.read_csv')
    def test_showEducationClients(self, mock_read_csv):
        # Cenário 1: Testa se a resposta é correta quando há dados válidos
        mock_read_csv.return_value = pd.DataFrame({
            'education': ['tertiary', 'secondary', 'primary', 'tertiary', 'secondary']
        })
        response = self.client.get('/educationclients')
        self.assertEqual(response.status_code, 200)
        self.assertIn('tertiary', response.json['labels'])
        print("Cenário 1: Resposta com dados válidos para /educationclients:", response.json)

        # Cenário 2: Testa se a resposta é correta quando não há dados
        mock_read_csv.return_value = pd.DataFrame({'education': []})
        response = self.client.get('/educationclients')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['labels'], [])
        print("Cenário 2: Resposta sem dados para /educationclients:", response.json)

        # Cenário 3: Testa se a resposta é correta quando há um erro na leitura do CSV
        mock_read_csv.side_effect = Exception("Error reading CSV")
        response = self.client.get('/educationclients')
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], "Error reading CSV")
        print("Cenário 3: Resposta com erro na leitura do CSV:", response.json)

    @patch('pandas.read_csv')
    def test_showMaritalStatusClients(self, mock_read_csv):
        # Cenário 1: Testa se a resposta é correta quando há dados válidos
        mock_read_csv.return_value = pd.DataFrame({
            'marital': ['single', 'married', 'single', 'divorced', 'married']
        })
        response = self.client.get('/maritalstatusclients')
        self.assertEqual(response.status_code, 200)
        self.assertIn('single', response.json['labels'])
        print("Cenário 1: Resposta com dados válidos para /maritalstatusclients:", response.json)

        # Cenário 2: Testa se a resposta é correta quando não há dados
        mock_read_csv.return_value = pd.DataFrame({'marital': []})
        response = self.client.get('/maritalstatusclients')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['labels'], [])
        print("Cenário 2: Resposta sem dados para /maritalstatusclients:", response.json)

        # Cenário 3: Testa se a resposta é correta quando há um erro na leitura do CSV
        mock_read_csv.side_effect = Exception("Error reading CSV")
        response = self.client.get('/maritalstatusclients')
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], "Error reading CSV")
        print("Cenário 3: Resposta com erro na leitura do CSV:", response.json)


    @patch('app.routes.render_template')
    def test_predict_missing_fields(self, mock_render_template):
        # Cenário 1: Testa se a resposta é correta quando um campo obrigatório está faltando
        with self.app.test_request_context('/predict', method='POST', data={
            'age': 30,
            'balance': 1000,
            'duration': 100,
            'campaign': 1,
            'pdays': 5
            # 'previous' está faltando
        }):
            response, status_code = predict()
            self.assertEqual(status_code, 400)
            self.assertIn('400 Bad Request', response.json['error'])
            print("Cenário 1: Resposta para campo obrigatório faltando:", response.json)

        # Cenário 2: Testa se a resposta é correta quando todos os campos estão presentes
        mock_render_template.return_value = 'Há chances de subscrição'
        with self.app.test_request_context('/predict', method='POST', data={
            'age': 30,
            'balance': 1000,
            'duration': 100,
            'campaign': 1,
            'pdays': 5,
            'previous': 0
        }):
            response = predict()
            self.assertIn('Há chances de subscrição', response)
            print("Cenário 2: Resposta quando todos os campos estão presentes:", response)

        # Cenário 3: Testa se a resposta é correta quando todos os campos estão presentes mas com valores extremos
        with self.app.test_request_context('/predict', method='POST', data={
            'age': 150,
            'balance': -1000,
            'duration': 10000,
            'campaign': 100,
            'pdays': -1,
            'previous': 10
        }):
            response = predict()
            self.assertIn('Há chances de subscrição', response)
            print("Cenário 3: Resposta para valores extremos:", response)

if __name__ == '__main__':
    unittest.main()
