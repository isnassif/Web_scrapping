import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

# print(dados_pagina.prettify()) - Essa linha é responsável por pegar todo o código em HTML de uma página, código esse que também pode ser acessado através do google

# Primeira maneira de encontrar as frases da página

frases_pagina = dados_pagina.find_all('div', class_ = "quote")

for div in frases_pagina:
    texto = div.find('span', class_ ="text").text
    print(texto)

# Segunda maneira de encontrar as frases da página

frases_pagina2 = dados_pagina.find_all('span', itemprop = 'text') # Aqui eu procuro diretamento pelo itemprop o conteúdo das frases

for span in frases_pagina2:
    print(span.text)
