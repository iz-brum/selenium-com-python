from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

# Inicializando o navegador Firefox
firefox = Firefox()

# Definindo a URL
url = 'http://selenium.dunossauro.live/aula_05_a.html'

# Acessando a URL no navegador
firefox.get(url)

# Encontrando o elemento com ID 'python' e imprimindo o texto
div_py = firefox.find_element(By.ID, 'python')
pprint(div_py.text)

# Encontrando o elemento com ID 'haskell' e imprimindo o texto
div_haskell = firefox.find_element(By.ID, 'haskell')
pprint(div_haskell.text)

# Esperando 2 segundos
sleep(2)

# Fechando o navegador
firefox.quit()
