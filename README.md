/* Estilização da Imagem e Legenda */
figure { 
    margin: 20px 0; 
    display: flex;             /* Transforma em flexbox para facilitar o alinhamento */
    flex-direction: column;    /* Coloca imagem e legenda em coluna */
    align-items: center;       /* Centraliza os itens horizontalmente */
}

img { 
    width: 400px; 
    height: 400px; 
    object-fit: cover; 
    border-radius: 8px;
    border: 1px solid #ddd;
}

figcaption { 
    font-size: 0.9em; 
    color: #666; 
    margin-top: 8px; 
    font-style: italic;
    text-align: center;       /* <--- Isso garante a centralização do texto */
    width: 100%;              /* Garante que ele ocupe a largura disponível para alinhar */
}

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

  <figure>
        <img src="https://github.com/user-attachments/assets/5fee6a63-667f-432d-886c-15c4ac29ad14" alt="Saída do código no terminal">
        <figcaption>Figura 1: Demonstração da saída visual do script capturando as frases do site.</figcaption>
    </figure>

    
</section>
