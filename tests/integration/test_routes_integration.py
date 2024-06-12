import unittest
from app import app

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        # Cria uma instância de aplicação Flask para simular o contexto da aplicação
        self.app = app.test_client()

    def test_home_page(self):
        # Cenário 1: Testa se a página inicial retorna o status code 200
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Página inicial está acessível.")

    def test_predict_endpoint(self):
        # Cenário 1: Testa se o endpoint de predição retorna o status code 200 para uma requisição válida
        valid_data = {
            'age': '30',
            'balance': '1000',
            'duration': '100',
            'campaign': '1',
            'pdays': '5',
            'previous': '0'
        }
        response = self.app.post('/predict', data=valid_data)
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Endpoint de predição está acessível com dados válidos.")

        # Cenário 2: Testa se o endpoint de predição retorna o status code 400 para dados inválidos
        invalid_data = {
            'age': 'invalid',
            'balance': '1000',
            'duration': '100',
            'campaign': '1',
            'pdays': '5',
            'previous': '0'
        }
        response = self.app.post('/predict', data=invalid_data)
        self.assertEqual(response.status_code, 400)
        print("Cenário 2: Endpoint de predição retorna status code 400 para dados inválidos.")

        # Cenário 3: Testa se o endpoint de predição retorna uma mensagem de erro para dados inválidos
        response_data = response.get_json()
        self.assertIn('400 Bad Request', response_data['error'])
        print("Cenário 3: Endpoint de predição retorna mensagem de erro para dados inválidos.")

    def test_ecclientes_endpoint(self):
        # Cenário 1: Testa se o endpoint '/ecclientes' retorna o status code 200
        response = self.app.get('/ecclientes')
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Endpoint '/ecclientes' está acessível.")

        # Cenário 2: Testa se o endpoint '/ecclientes' retorna um JSON com as contagens de trabalho (job)
        response_data = response.get_json()
        self.assertIn('labels', response_data)
        self.assertIn('values', response_data)
        print("Cenário 2: Endpoint '/ecclientes' retorna contagens de trabalho (job).")

        # Cenário 3: Testa se o endpoint '/ecclientes' retorna valores numéricos nas contagens
        self.assertTrue(all(isinstance(value, int) for value in response_data['values']))
        print("Cenário 3: Endpoint '/ecclientes' retorna valores numéricos nas contagens.")

    def test_educationclients_endpoint(self):
        # Cenário 1: Testa se o endpoint '/educationclients' retorna o status code 200
        response = self.app.get('/educationclients')
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Endpoint '/educationclients' está acessível.")

        # Cenário 2: Testa se o endpoint '/educationclients' retorna um JSON com as contagens de educação (education)
        response_data = response.get_json()
        self.assertIn('labels', response_data)
        self.assertIn('values', response_data)
        print("Cenário 2: Endpoint '/educationclients' retorna contagens de educação (education).")

        # Cenário 3: Testa se o endpoint '/educationclients' retorna valores numéricos nas contagens
        self.assertTrue(all(isinstance(value, int) for value in response_data['values']))
        print("Cenário 3: Endpoint '/educationclients' retorna valores numéricos nas contagens.")

    def test_maritalstatusclients_endpoint(self):
        # Cenário 1: Testa se o endpoint '/maritalstatusclients' retorna o status code 200
        response = self.app.get('/maritalstatusclients')
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Endpoint '/maritalstatusclients' está acessível.")

        # Cenário 2: Testa se o endpoint '/maritalstatusclients' retorna um JSON com as contagens de estado civil (marital)
        response_data = response.get_json()
        self.assertIn('labels', response_data)
        self.assertIn('values', response_data)
        print("Cenário 2: Endpoint '/maritalstatusclients' retorna contagens de estado civil (marital).")

        # Cenário 3: Testa se o endpoint '/maritalstatusclients' retorna valores numéricos nas contagens
        self.assertTrue(all(isinstance(value, int) for value in response_data['values']))
        print("Cenário 3: Endpoint '/maritalstatusclients' retorna valores numéricos nas contagens.")

    def test_showEducationClients(self):
        # Cenário 1: Testa se o endpoint '/educationclients' retorna o status code 200
        response = self.app.get('/educationclients')
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Endpoint '/educationclients' está acessível.")

        # Cenário 2: Testa se o endpoint '/educationclients' retorna um JSON com as contagens de educação (education)
        response_data = response.get_json()
        self.assertIn('labels', response_data)
        self.assertIn('values', response_data)
        print("Cenário 2: Endpoint '/educationclients' retorna contagens de educação (education).")

        # Cenário 3: Testa se o endpoint '/educationclients' retorna valores numéricos nas contagens
        self.assertTrue(all(isinstance(value, int) for value in response_data['values']))
        print("Cenário 3: Endpoint '/educationclients' retorna valores numéricos nas contagens.")

    def test_showMaritalStatusClients(self):
        # Cenário 1: Testa se o endpoint '/maritalstatusclients' retorna o status code 200
        response = self.app.get('/maritalstatusclients')
        self.assertEqual(response.status_code, 200)
        print("Cenário 1: Endpoint '/maritalstatusclients' está acessível.")

        # Cenário 2: Testa se o endpoint '/maritalstatusclients' retorna um JSON com as contagens de estado civil (marital)
        response_data = response.get_json()
        self.assertIn('labels', response_data)
        self.assertIn('values', response_data)
        print("Cenário 2: Endpoint '/maritalstatusclients' retorna contagens de estado civil (marital).")

        # Cenário 3: Testa se o endpoint '/maritalstatusclients' retorna valores numéricos nas contagens
        self.assertTrue(all(isinstance(value, int) for value in response_data['values']))
        print("Cenário 3: Endpoint '/maritalstatusclients' retorna valores numéricos nas contagens.")


if __name__ == '__main__':
    unittest.main()
