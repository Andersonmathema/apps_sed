from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()


def carregar_selenium():
    #navegador = opcoesSelenium.Chrome()
    chrome_options = opcoesSelenium.ChromeOptions()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')  # Necessário para Windows
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    navegador = opcoesSelenium.Chrome(options=chrome_options)
    return navegador
    
    
def login():    
    # Obter os valores das variáveis de ambiente
    navegador = carregar_selenium()
    password = os.getenv('PASSWORD')
    documento = os.getenv('DOCUMENTO')
    navegador.get('https://cmsp.ip.tv/')
    time.sleep(5)
    try:
        navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/form/div/div[1]/div/div').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '//*[@id=":r4:"]/li[1]').click()
        time.sleep(2)
        navegador.find_element(By.ID, 'document').send_keys(documento)
        time.sleep(2)
        navegador.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/form/div/div[5]/button').click()
        time.sleep(5)

        # Atividades
        navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/button').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/div/div/div/ul/li[2]/a').click()
        time.sleep(2)

        navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[2]').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[3]').click()
        time.sleep(3)
        tabela = navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div/div/table')
        time.sleep(2)
        linhas = tabela.find_elements(By.TAG_NAME, 'tr')          
        time.sleep(2)
        dados = []
        ids = []
        for linha_atual in linhas:
            colunas = linha_atual.find_elements(By.TAG_NAME, 'td')
            linha_dados = [coluna.text for coluna in colunas]
            dados.append(linha_dados)
        del dados[0]
        for id in dados:           
            ids.append(id[8])
        
        for id in ids:
            navegador.find_element(By.XPATH, f'//*[@id="{id}"]/div/button').click()
            time.sleep(2)     

            navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[3]/div[2]').click()
            time.sleep(3)
            navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/button[2]').click()
            time.sleep(3)
            checkbox = navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/span/span[1]/input')
            if checkbox.is_selected():  # Verifica se o checkbox está checado
                checkbox.click()  # Clica para desmarcar
                time.sleep(2)
                navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/button[2]').click()
                time.sleep(3)
            else:
                navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/button[1]').click()
                time.sleep(3)

            # salva a mudança de data
            navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/button[2]').click()
            time.sleep(3)
            
            navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/button[1]').click()
            time.sleep(3)
            navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[2]').click()
            time.sleep(2)
            navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[3]').click()
            time.sleep(3)

        navegador.quit()       

    except Exception as e:
        print(e)


if __name__ == '__main__':
    login()
    