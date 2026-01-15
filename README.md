<h1>Web_scrapping</h1>
<p>Olá! Esse é meu repositório de web scraping, aqui você vai encontrar os meus testes e o meu caminho de aprendizado nessa tecnologia. Na pasta <strong>"Codes"</strong> você pode conferir o código de cada um dos projetos. Abaixo, apresento o relatório detalhado das funcionalidades.</p>

<section class="container">
    <h2>1. Web_scraping_1</h2>
    <p>Esse foi o primeiro arquivo feito, utiliza web scraping de forma muito básica, faz a raspagem do site <em>"Quotes to scrape"</em> que contém algumas frases de figuras famosas. Como foi o primeiro arquivo feito, ele ainda é muito básico, não contém headers e tem apenas uma funcionalidade, buscar as frases presentes no site, essa busca acontece de duas maneiras (ambas no arquivo):</p>
     <div class="metodo">
        <ul>
            <li>
                <strong>Busca Hierárquica (Div > Span):</strong> 
                Consiste em localizar as <code>divs</code> de classe <code>"quote"</code> para então filtrar o <code>span</code> de classe <code>"text"</code>. 
                <em>Vantagem:</em> Ideal para extrair múltiplos dados correlacionados (autor, tags). 
                <em>Desvantagem:</em> Maior custo computacional por realizar duas buscas.
            </li>
            <li>
                <strong>Busca Direta (Itemprop):</strong> 
                Localiza diretamente os elementos com a marcação <code>itemprop="text"</code>.
                <em>Vantagem:</em> Maior rapidez e eficiência na execução do script.
            </li>
        </ul>
    </div>

  
<div align="center">
      <img src="https://github.com/user-attachments/assets/5fee6a63-667f-432d-886c-15c4ac29ad14" width="400" height="400" style="object-fit: cover;">
      <br>
      <em>Figura 1: Saída visual do script com ambas as buscas. </em>
    </div>


<h2>2. Web_scraping_mercado_livre</h2>
<p>Este projeto representa uma evolução significativa em relação ao primeiro, introduzindo conceitos essenciais para raspagem de dados em sites dinâmicos e de grande porte. O script realiza a busca de produtos no Mercado Livre, extraindo nomes, preços e links de forma automatizada, nesse projeto em específico, o código busca pelo celular iphone 15</p>

<div class="metodo">
    <ul>
        <li>
            <strong>Uso de Headers (User-Agent):</strong> 
            Diferente do projeto anterior, aqui foi implementado um cabeçalho que simula uma requisição feita por um navegador real. Isso é fundamental para evitar bloqueios por sistemas anti-bot.
        </li>
        <li>
            <strong>Tratamento de URL Dinâmica:</strong> 
            O código recebe o nome do produto via entrada do usuário e trata espaços em branco, formatando a URL para o padrão do Mercado Livre.
        </li>
        <li>
            <strong>Loop de Paginação Automatizado:</strong> 
            Implementação de uma lógica de repetição que navega pelas páginas de resultados (incrementando o índice de 48 em 48 produtos), parando automaticamente quando não encontra mais descrições no site.
        </li>
        <li>
            <strong>Zipagem de Dados:</strong> 
            Utilização da função <code>zip()</code> para iterar simultaneamente sobre listas de nomes, preços e links, garantindo a integridade da relação entre os dados.
        </li>
    </ul>
</div>

<div align="center">
      <img src="https://github.com/user-attachments/assets/be8b1349-b48c-45f5-8324-dfee8852a454" width="400" height="400" style="object-fit: cover;">
      <br>
      <em>Figura 2: Parte do resultado da busca pelo celular. </em>
    </div>

<h2>3. Web_scraping_soccer</h2>
<p>Este projeto aborda um dos maiores desafios do web scraping moderno: a extração de dados de sites que utilizam carregamento dinâmico via JavaScript. O objetivo aqui foi capturar estatísticas detalhadas du uma partida de futebol no site SofaScore.</p>

<div class="metodo">
    <ul>
        <li>
            <strong>Limitação do Requests:</strong> 
            O primeiro teste (comentado no código) demonstrou que o uso simples da biblioteca <code>requests</code> falha em sites com proteções complexas ou carregamento assíncrono, resultando em dados incompletos ou erros de acesso.
        </li>
        <li>
            <strong>Automação com Playwright:</strong> 
            Para contornar o problema, implementei o <strong>Playwright</strong>. Ele simula um navegador real (Chromium) que carrega a página completa, executa o JavaScript e gera os cookies/tokens necessários para validar a requisição.
        </li>
        <li>
            <strong>Injeção de Script (Page Evaluate):</strong> 
            Utilizei o método <code>page.evaluate</code> para executar um <code>fetch</code> diretamente no contexto do navegador. Isso permite capturar os dados da API interna do site já autenticado, garantindo o acesso aos arquivos JSON.
        </li>
        <li>
            <strong>Exportação para Pandas/Excel:</strong> 
            Após o tratamento dos dados estruturados em JSON, utilizei a biblioteca <strong>Pandas</strong> para organizar as estatísticas (como posse de bola, chutes e faltas) em um DataFrame e exportá-las para um arquivo <code>.xlsx</code>.
        </li>
    </ul>
</div>

<div align="center">
      <img src="https://github.com/user-attachments/assets/59472962-40c3-4969-8bd8-f90741b89671" width="400" height="800" style="object-fit: cover;">
      <br>
      <em>Figura 3: Tabela gerada após extração dos dados do site. </em>
    </div>

</section>
