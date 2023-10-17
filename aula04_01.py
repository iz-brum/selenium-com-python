# Importando os módulos necessários
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

# Definindo a URL
url = 'https://selenium.dunossauro.live/aula_04_a.html'

# Inicializando o navegador Firefox
browser = Firefox()

# Acessando a URL
browser.get(url)

# Encontrando o primeiro elemento <ul> na página
unordered_list = browser.find_element(By.TAG_NAME, 'ul') #1

# Encontrando todos os elementos <li> dentro do <ul>
list = unordered_list.find_elements(By.TAG_NAME, 'li') #2

# Encontrando o primeiro elemento <a> dentro do primeiro <li>
list[0].find_element(By.TAG_NAME, 'a').text #3

"""
1. Buscamos 'ul'
2. Buscamos todos 'li'
3. No primeiro 'li', buscamos 'a' e pegamos o seu conteúdo (texto)

ul
    li
        a
            texto
    li
        a
            texto
"""

'''
Esse código acessa uma página web, encontra uma lista não ordenada (<ul>), em seguida, encontra todos os itens de lista (<li>) dentro dessa lista. Por fim, ele encontra o primeiro link (<a>) dentro do primeiro item de lista e imprime o texto contido nele.
'''