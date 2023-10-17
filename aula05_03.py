from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

# Definindo uma função para preencher o formulário e submetê-lo
def best_movie(browser, filme, email, telefone):
    browser.find_element(By.NAME, 'filme').send_keys(filme)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'enviar').click()

# Inicializando o navegador Firefox
firefox = Firefox()

# Definindo a URL
url = 'http://selenium.dunossauro.live/aula_05_c.html'

# Acessando a URL no navegador
firefox.get(url)

# Esperando 0.8 segundos
sleep(0.8)

# Chamando a função best_movie para preencher o formulário
best_movie(firefox, 'Coherence', 'email', '(065)99999-9999')

# Esperando 5 segundos
sleep(5)

# Fechando o navegador
firefox.quit()
