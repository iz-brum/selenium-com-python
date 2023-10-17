from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

# Inicializando o navegador Firefox
firefox = Firefox()

# Definindo a URL
url = 'http://selenium.dunossauro.live/aula_05_b.html'

# Acessando a URL no navegador
firefox.get(url)

# Encontrando o elemento com a classe 'topico'
topico = firefox.find_element(By.CLASS_NAME, 'topico')

# Encontrando todos os elementos com a classe 'linguagens'
linguagens = firefox.find_elements(By.CLASS_NAME, 'linguagens')

# Iterando sobre os elementos 'linguagens'
for linguagem in linguagens:
    # Obtendo o nome da linguagem e a data de criação
    nome_linguagem = linguagem.find_element(By.TAG_NAME, 'h2').text
    data_criacao = linguagem.find_element(By.TAG_NAME, 'p').text
    
    # Imprimindo as informações
    pprint((nome_linguagem, data_criacao))

# Esperando 2 segundos
sleep(2)

# Fechando o navegador
firefox.quit()
