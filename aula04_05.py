# Importando os módulos necessários
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

''' LINHA 6
1. Pegar todos os links de aulas
   {'nome da aula': 'link da aula'} 
2. Navegar até o exercício 3
   Encontrar a url do exercício 3 e caminhar até ele 
'''

# Definindo uma função chamada get_links que retorna um dicionário de links
def get_links(browser, element):
    ''' LINHA 14
    Pega todos os links de um elemento

    - browser = a instância do navegador
    - element = webelement ['aside', 'main', 'body', 'ul', 'ol', ...]
    ''' 
    listaDeAncoras = {}  # Inicializa um dicionário vazio
    elemento = browser.find_element(By.TAG_NAME, element)  # Encontra o elemento especificado
    ancoras = elemento.find_elements(By.TAG_NAME, 'a')  # Encontra todos os links dentro desse elemento
    
    # Itera sobre os links encontrados
    for ancora in ancoras:
        # Adiciona ao dicionário o texto do link como chave e o URL como valor
        listaDeAncoras[ancora.text] = ancora.get_attribute('href')
    
    return listaDeAncoras

# Define a URL que será usada
url = 'https://selenium.dunossauro.live/aula_04.html'

# Inicia o navegador Firefox
browser = Firefox()
browser.get(url)  # Abre a URL
sleep(1.5)  # Espera 1.5 segundos para garantir que a página carregue completamente

'''
Parte 1 
'''
# Chama a função get_links para encontrar os links dentro do elemento 'aside'
aulas = get_links(browser, 'aside')
pprint(aulas)  # Imprime os links encontrados

# Chama a função get_links para encontrar os links dentro do elemento 'main'
exercicios = get_links(browser, 'main')
pprint(exercicios)  # Imprime os links encontrados

'''
Parte 2
'''
# Navega até o exercício 3 usando o link obtido anteriormente
browser.get(exercicios['Exercício 3'])

sleep(10)  # Espera 10 segundos
browser.quit()  # Fecha o navegador
