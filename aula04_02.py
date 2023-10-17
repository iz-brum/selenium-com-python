# Importando os módulos necessários
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

# Definindo uma função para encontrar elementos por texto
def find_by_text(browser, tag, text): 
    """
    Encontrar o elemento com o texto `text`.

    Argumentos:
        - browser = Instância do browser [firefox, chrome, ...]
        - tag     = Tag onde o texto será procurado
        - texto   = Conteúdo que deve estar na tag
    """

    elementos = browser.find_elements(By.TAG_NAME, tag) # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento

# Definindo uma função para encontrar elementos por link
def find_by_href(browser, link):
    """
    Encontrar o elemento 'a' com o link `link`.

    Argumentos:
        - browser = Instância do browser [firefox, chrome, ...]
        - link    = Link que será procurado em todas as tags 'a'
    """
    elementos = browser.find_elements(By.TAG_NAME, 'a') # lista

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

# Definindo a URL
url = 'https://selenium.dunossauro.live/aula_04_a.html'

# Inicializando o navegador Firefox
browser = Firefox()

# Acessando a URL
browser.get(url)

# Esperando por 2 segundos
sleep(2)

# Chamando a função para encontrar o elemento com texto 'DuckDuckGo'
elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')

# Chamando a função para encontrar o elemento com o link contendo 'ddg'
# elemento_ddg = find_by_href(browser, 'ddg')


'''
Este código define duas funções para encontrar elementos na página web usando Selenium. A função find_by_text busca elementos pelo texto que contêm, e a função find_by_href busca elementos pelo link (URL) que contêm. A URL atual é definida na variável url, e o navegador Firefox é inicializado para abrir esta URL. Após 2 segundos, a função find_by_text é chamada para encontrar um elemento com o texto 'DuckDuckGo'w
'''