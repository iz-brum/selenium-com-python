# Importando as bibliotecas necessárias
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

# Definindo a URL
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

# Inicializando o navegador Firefox
browser = Firefox()

# Acessando a URL
browser.get(url)

# Aguardando 2 segundos para garantir que a página carregue completamente
sleep(2)

# Encontrando o primeiro elemento <a> na página
a = browser.find_element(By.TAG_NAME, "a")

# Encontrando o primeiro elemento <p> na página
p = browser.find_element(By.TAG_NAME, "p")
print(f'Conteúdo da primeira tag p: {p.text}\n')

# Loop de 1 a 10
for i in range(1,11):
    # Clicando no elemento <a>
    a.click()
    
    # Encontrando todos os elementos <p> na página após o clique
    p = browser.find_elements(By.TAG_NAME, "p")
    
    # Imprimindo os valores
    print(f'Valor de p: {p[i].text} Valor de click: {i}')
    print(f'Os valores são iguais? {p[i].text == str(i)}')

# Imprimindo o conteúdo do elemento <a>
print(f'\nConteúdo da tag a: {a.text}')

# Aguardando 60 segundos antes de fechar o navegador (apenas para visualizar o resultado)
sleep(60)

# Fechando o navegador
browser.quit()
