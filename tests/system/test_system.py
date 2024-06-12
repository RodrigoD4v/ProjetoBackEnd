import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class TestSystem(unittest.TestCase):

    def test_home_page(self):
        # Cenário 1: Testa se a página inicial é acessível
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) 
        driver.get("https://projetobackend-production.up.railway.app/")
        self.assertIn("Predição de Modelo ML", driver.title)
        driver.quit()
        print("Cenário 1: Página inicial está acessível.")

    def test_fields_presence(self):
        # Cenário 1: testa se os campos estão presentes
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) 
        driver.get("https://projetobackend-production.up.railway.app/")
        # Localiza os elementos na página pelos seus IDs
        age_field = driver.find_element(By.XPATH, '//*[@id="age"]')
        balance_field = driver.find_element(By.XPATH, '//*[@id="balance"]')
        duration_field = driver.find_element(By.XPATH, '//*[@id="duration"]')
        pdays_field = driver.find_element(By.XPATH, '//*[@id="pdays"]')
        previous_field = driver.find_element(By.XPATH, '//*[@id="previous"]')
        campaign_field = driver.find_element(By.XPATH, '//*[@id="campaign"]')
        predict_button = driver.find_element(By.XPATH, '//*[@id="btn-predict"]')
        
        # Verifica se os campos foram encontrados na página
        self.assertTrue(age_field.is_displayed(), "Campo de idade não encontrado")
        self.assertTrue(balance_field.is_displayed(), "Campo de saldo não encontrado")
        self.assertTrue(duration_field.is_displayed(), "Campo de duração não encontrado")
        self.assertTrue(pdays_field.is_displayed(), "Campo de pdays não encontrado")
        self.assertTrue(previous_field.is_displayed(), "Campo de previous não encontrado")
        self.assertTrue(campaign_field.is_displayed(), "Campo de campaign não encontrado")
        self.assertTrue(predict_button.is_displayed(), "Botão de previsão não encontrado")

        driver.quit()

        # Imprime uma mensagem quando o teste passa
        print("Cenário 1: Teste de presença de campos passou com sucesso.")

    def test_prediction_page(self):
        # Cenário 1: Testa a funcionalidade de previsão
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) 
        driver.get("https://projetobackend-production.up.railway.app/")
        
        # Localiza os elementos na página
        age_field = driver.find_element(By.XPATH, '//*[@id="age"]')
        balance_field = driver.find_element(By.XPATH, '//*[@id="balance"]')
        duration_field = driver.find_element(By.XPATH, '//*[@id="duration"]')
        pdays_field = driver.find_element(By.XPATH, '//*[@id="pdays"]')
        previous_field = driver.find_element(By.XPATH, '//*[@id="previous"]')
        campaign_field = driver.find_element(By.XPATH, '//*[@id="campaign"]')
        predict_button = driver.find_element(By.XPATH, '//*[@id="btn-predict"]')
        
        # Preenche os campos com valores específicos
        age_field.send_keys("30")
        balance_field.send_keys("5000")
        duration_field.send_keys("5")
        pdays_field.send_keys("10")
        previous_field.send_keys("0")
        campaign_field.send_keys("1")
        
        # Clica no botão de prever
        predict_button.click()
        
        # Verifica se o resultado da previsão é exibido corretamente
        result_element = driver.find_element(By.XPATH, '//*[@id="title"]')
        self.assertTrue(result_element.is_displayed(), "Elemento de título não encontrado")
        self.assertEqual(result_element.text.lower(), "resultado predição", "Texto do título incorreto")
        
        driver.quit()

        # Imprime uma mensagem quando o teste passa
        print("Teste de previsão passou com sucesso.")

    def test_chart_presence(self):
        # Cenário 1: Testa a presença dos gráficos
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) 
        driver.get("https://projetobackend-production.up.railway.app/")
        
        # Localiza os elementos dos gráficos na página
        bar_chart = driver.find_element(By.XPATH, '//*[@id="barChart"]')
        horizontal_bar_chart = driver.find_element(By.XPATH, '//*[@id="horizontalBarChart"]')
        line_chart = driver.find_element(By.XPATH, '//*[@id="lineChart"]')
        
        # Verifica se os gráficos foram encontrados na página
        self.assertTrue(bar_chart.is_displayed(), "Gráfico de barras não encontrado")
        self.assertTrue(horizontal_bar_chart.is_displayed(), "Gráfico de barras horizontais não encontrado")
        self.assertTrue(line_chart.is_displayed(), "Gráfico de linha não encontrado")
        
        driver.quit()

        # Imprime uma mensagem quando o teste passa
        print("Teste de presença dos gráficos passou com sucesso.")

    def test_matching_values(self):
        # Cenário 1: Testa a consistência dos dados
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) 
        driver.get("https://projetobackend-production.up.railway.app/")
        
        # Localiza os elementos na página
        age_field = driver.find_element(By.XPATH, '//*[@id="age"]')
        balance_field = driver.find_element(By.XPATH, '//*[@id="balance"]')
        duration_field = driver.find_element(By.XPATH, '//*[@id="duration"]')
        pdays_field = driver.find_element(By.XPATH, '//*[@id="pdays"]')
        previous_field = driver.find_element(By.XPATH, '//*[@id="previous"]')
        campaign_field = driver.find_element(By.XPATH, '//*[@id="campaign"]')
        predict_button = driver.find_element(By.XPATH, '//*[@id="btn-predict"]')

        age_value = "30"
        balance_value = "5000"
        duration_value = "5"
        pdays_value = "10"
        previous_value = "0"
        campaign_value = "1"
        
        # Preenche os campos com valores específicos
        age_field.send_keys(age_value)
        balance_field.send_keys(balance_value)
        duration_field.send_keys(duration_value)
        pdays_field.send_keys(pdays_value)
        previous_field.send_keys(previous_value)
        campaign_field.send_keys(campaign_value)

        # Clica no botão de prever
        predict_button.click()

        # Obter o texto dentro do elemento <div id="data-input-el">
        data_input_element = driver.find_element(By.XPATH, '//*[@id="data-input-el"]')
        data_input_text = data_input_element.text
        
        # Extrair os valores específicos do texto obtido
        age_text = data_input_text.split('Idade: ')[1].split('\n')[0]
        balance_text = data_input_text.split('Saldo: ')[1].split('\n')[0]
        duration_text = data_input_text.split('Duração: ')[1].split('\n')[0]
        pdays_text = data_input_text.split('Dias: ')[1].split('\n')[0]
        previous_text = data_input_text.split('Anterior: ')[1].split('\n')[0]
        campaign_text = data_input_text.split('Campanha: ')[1].split('\n')[0]

        # Verificar se os valores inseridos correspondem aos valores exibidos no texto
        self.assertEqual(age_value, age_text, "Valor de idade incorreto")
        self.assertEqual(balance_value, balance_text, "Valor de saldo incorreto")
        self.assertEqual(duration_value, duration_text, "Valor de duração incorreto")
        self.assertEqual(pdays_value, pdays_text, "Valor de pdays incorreto")
        self.assertEqual(previous_value, previous_text, "Valor de previous incorreto")
        self.assertEqual(campaign_value, campaign_text, "Valor de campaign incorreto")
        
        # Verifica se o resultado da previsão é exibido corretamente
        result_element = driver.find_element(By.XPATH, '//*[@id="title"]')
        self.assertTrue(result_element.is_displayed(), "Elemento de título não encontrado")
        self.assertEqual(result_element.text.lower(), "resultado predição", "Texto do título incorreto")
        
        driver.quit()

        # Imprime uma mensagem quando o teste passa
        print("Teste de correspondência de valores.")

if _name_ == '_main_':
    unittest.main()