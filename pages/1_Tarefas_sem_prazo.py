from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st
import tempfile
import time
import os



# Inicialize a chave 'temp_file_path' no session_state se ainda não existir
if 'temp_file_path' not in st.session_state:
    st.session_state['temp_file_path'] = None

# Função para armazenar credenciais em um arquivo temporário
def salvar_credenciais(username, password):
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write(f'username={username}\npassword={password}')
        return temp_file.name  # Retorna o caminho do arquivo temporário

# Função para ler as credenciais do arquivo temporário
def ler_credenciais(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        credentials = file.read()
        # Transformar as credenciais em um dicionário
        creds_dict = dict(line.split('=') for line in credentials.splitlines())
        return creds_dict

# Função para deletar o arquivo temporário
def deletar_arquivo(caminho_arquivo):
    try:
        os.remove(caminho_arquivo)
        st.success("Senhas apagadas com sucesso!")
    except Exception as e:
        st.error(f"Erro ao deletar o arquivo: {e}")

# Função para carregar o navegador Selenium com as opções desejadas
def carregar_selenium():
    #navegador = opcoesSelenium.Chrome()
    chrome_options = opcoesSelenium.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    navegador = opcoesSelenium.Chrome(options=chrome_options)
    return navegador

# Função de login que tenta autenticar e, se falhar, retorna ao fluxo de entrada de dados
def login(documento, password):
    navegador = carregar_selenium()
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

        # Verificar a presença do elemento de falha de login usando WebDriverWait
        try:
            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div'))
            )
            st.error("Falha no login. Por favor, verifique suas credenciais e tente novamente.")
            navegador.quit()
            return False  # Indica que o login falhou e precisa ser tentado novamente
        except:
            st.success("Login efetuado com sucesso!")
            
             # Adiciona uma barra de progresso após o login bem-sucedido
            progress_text = "Operação em progresso. Isso pode levar cerca de 30 minutos. Por favor, aguarde."
            my_bar = st.progress(0, text=progress_text)

            # Simulação de um processo longo, atualizando a barra de progresso lentamente
            total_steps = 1800  # Total de segundos para um processo de 30 minutos
            for step in range(total_steps):
                # Aqui você pode adicionar suas operações reais
                time.sleep(1)  # Simula 1 segundo de trabalho por etapa
                progress = (step + 1) / total_steps * 100  # Calcula o progresso em porcentagem
                my_bar.progress(int(progress), text=progress_text)

            # Conclui o processo e limpa a barra de progresso
            my_bar.empty()

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
        st.error(f"Erro durante o processo de login: {e}")
        navegador.quit()
        return False  # Indica que ocorreu um erro e precisa tentar novamente
    
    return True  # Indica que o login foi bem-sucedido

if __name__ == '__main__':
    # Interface do Streamlit para capturar o login e senha
    st.title("Removedor de prazos do Tarefas SP")
    
    # Campos de entrada para o usuário
    username = st.text_input("RG com dígito")
    password = st.text_input("Senha", type="password")

    # Botão de login
    if st.button("Entrar"):
        if username and password:
            # Salvar as credenciais em um arquivo temporário
            temp_file_path = salvar_credenciais(username, password)
            st.success("Credenciais salvas com sucesso! Não se preocupe, elas serão apagadas ao final do processo!")
            st.session_state['temp_file_path'] = temp_file_path  # Salvar o caminho na sessão
        else:
            st.error("Por favor, insira o nome o RG com dígito e a senha.")

    # Verificar se há um caminho salvo no session_state e tentar login
    if st.session_state['temp_file_path']:
        credenciais = ler_credenciais(st.session_state['temp_file_path'])
        login_sucesso = login(credenciais.get('username'), credenciais.get('password'))
        
        # Excluir o arquivo temporário após o uso
        deletar_arquivo(st.session_state['temp_file_path'])
        st.session_state['temp_file_path'] = None  # Remover o caminho da sessão
        
        # Se o login falhar, mostre uma mensagem para o usuário tentar novamente
        if not login_sucesso:
            st.warning("Tente novamente digitando suas credenciais corretamente.")
