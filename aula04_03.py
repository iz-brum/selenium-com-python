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

    elementos = browser.find_elements(By.TAG_NAME, tag) # Lista de elementos

    for elemento in elementos:
        if elemento.text == text:
            return elemento

# Definindo a URL, a tag e uma lista de textos
url = 'https://selenium.dunossauro.live/aula_04_b.html'
tag = 'div'
vet = ['um', 'dois', 'tres', 'quatro']

# Inicializando o navegador Firefox
browser = Firefox()

# Acessando a URL
browser.get(url)

# Iterando sobre os elementos da lista 'vet'
for i in vet:
    sleep(0.4)
    find_by_text(browser, tag, i).click()

# Navegando para trás no histórico do navegador
for i in vet:
    sleep(0.4)
    browser.back()

# Navegando para frente no histórico do navegador
for i in vet:
    sleep(0.4)
    browser.forward()

'''
Neste código, a função find_by_text é definida para localizar elementos na página pelo texto que contêm. Em seguida, a URL, a tag e uma lista de textos são definidos. O navegador Firefox é inicializado e a URL é acessada. Em seguida, o código itera sobre a lista 'vet', clicando em cada elemento com o texto correspondente. Em seguida, ele navega para trás e para frente no histórico do navegador usando os comandos browser.back() e browser.forward(). Cada ação é precedida por um intervalo de 0.4 segundos de espera usando sleep(0.4).
'''
