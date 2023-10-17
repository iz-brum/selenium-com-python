from selenium.webdriver import Firefox  # Importa a classe Firefox do módulo selenium.webdriver
from selenium.webdriver.common.by import By  # Importa a classe By do módulo selenium.webdriver.common.by
from time import sleep  # Importa a função sleep do módulo time
from urllib.parse import urlparse  # Importa a função urlparse do módulo urllib.parse

# Define a variável url como uma string com o endereço 'https://selenium.dunossauro.live/aula_04_b.html'
url = 'https://selenium.dunossauro.live/aula_04_b.html'

# Cria uma instância do navegador Firefox e a atribui à variável browser
browser = Firefox()

# Abre a página contida na variável url no navegador
browser.get(url)

# Utiliza a função urlparse para analisar o URL atual e armazena o resultado em url_parsed
url_parsed = urlparse(browser.current_url)
