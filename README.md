# Web_scrapping

Olá! Esse é meu repositório de web scraping, na pasta "Codes" você pode conferir o código de cada um dos projetos que fiz, caso queria entender de forma mais explicada, leia o relatório a seguir, onde será explicado detalhadamente cada um dos códigos e suas funcionalidades


1. Web_scraping_1

Esse foi o primeiro arquivo feito, utiliza web scraping de forma muito básica, faz a raspagem do site "Quotes to scrape", que contém algumas frases de pessoas famosas. Como foi o primeiro arquivo feito, ele ainda é muito básico, não contém headers e tem apenas uma funcionalidade, buscar as frases presentes no site, essa busca acontece de duas maneiras (ambas no arquivo):

- A primeira é através da busca das divs com a classe "quote" e dentro delas a busca pelo span da classe "text", isso seria vantajoso se eu estivesse também procurando por informaçẽos além da frase, por exemplo, o nome do autor, o ano da frase, etc. Mas é desvantajoso em relação ao custo, tendo em vista que são realizadas duas buscas

- A segunda é uma busca mais direta, tendi em vista que ela vai direto nos dados com a marcação de itemprop "text", isso torna a busca mais rápida e eficiente.

Abaixo segue a saída visual do código

<img width="1194" height="362" alt="image" src="https://github.com/user-attachments/assets/5fee6a63-667f-432d-886c-15c4ac29ad14" />
