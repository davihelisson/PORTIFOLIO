
# DESAFIO DE PROJETO - DESAFIO 02

## Módulo 05 - Data Analytics

O arquivo '.pbix' é o arquvivo de Power BI contendo as modificações do dash original. As modificações estão apresentadas abaixo de acordo com a página.

### 01 - Página Principal
* Inserção do botão de navegação para a próxima página.

### 02 - Página Lucro Details
* Duplicação da página Principal;
* Remoção dos visuais, mantendo apenas a seção de "Cabeçalho", alterando o título para "Profit Report Details".
* Inclusão de forma (quadrado com cantos arredondados) para dar destaque ao visual.
* Inclusão de Visual "Gráfico em Cascata" com o Trimestre no eixo "X" e a soma de Profit no eixo "Y".
* Inclusão de Visual "Treemap" com a categoria "Segment" e os valores como a "soma de Profit"
* Inclusão de Visual "Árvore Hieráquica". 
    1. No campo 'Analisar' coloquei a "soma de Profit";
    2. No campo 'Explicar por:' coloquei 'Date + Ano' e 'Country' (nessa ordem)
    3.  Posicionei a árvore de maneira a esconder os títulos da árvore abaixo da caixa do cabeçalho. Aparentemente esse visual não permite remover o título.
* Inclusão de Visual Personalisado "Chiclet Slicer" para selecionar o ano de análise (Categoria = ano). Sobrepus esse visual com a Árvore Hierárquica.
* Inclusão de botões de navegação (página anterior, próxima página, HOME). O botão "HOME" possui uma imagem que está sobreposta por um botão invisível.


### 03 - Página Product Details
* Duplicação do visual principal.
* Remoção de quase todos os visuais exceto o "Gráfico de Área" para representar as vendas ao longo do tempo. Para esse visual foi incluído uma forma para dar destaque.
* Inclusão de "Chiclet Slicer" (Categoria = Product) e deixei todos em uma única linha, sobrepostos ao cabeçalho.
* Inclusão de "Gráfico de Colunas" com 'Country' no eixo X, e 'Soma de Sales' e 'TOP 3 Product' no eixo Y. A coluna 'TOP 3 Product' foi criada como uma medida via DAX, conforme descrito abaixo:
>   
    TOP3 PRODUCT = CALCULATE([total sales], TOPN(3, ALL(financials[Product]), [total sales]), VALUES(financials[Product])) 

* Inclusão de Gráfico de barras laterais clusterizado para apresentar os 'Top 3 Produtos'. No eixo Y está "Product" e no eixo X está "Top3 Product".
* Inclusão de outro gráfico de barras laterais clusterizado para mostrar o total de produtos. No eixo Y está "Product" e no eixo X está "Soma de Sales".    
* Inclusão de botões de navegação (página anterior, próxima página, HOME). O botão "HOME" possui uma imagem que está sobreposta por um botão invisível.


### 04 - Página Sales per Country
* Duplicação da página "Lucro Details" e exclusão de visuais.
* Inclusão de Visual Personalisado "Sankey Chart" para mostrar as vendas por país e segmento. 
    1. No campo 'Origem' está a lista "Country";
    2. No campo 'Destino' está a lista "Segment"
    3. No campo 'Peso' está a "Soma de Sales".
* Inclusão de Gráfico de Barras Laterais clusterizado, mostrando "Vendas por Continente". No eixo X está "Country", no eixo Y está "Soma de Sales" e no campo 'legenda' está o grupo "Continentes". Esse grupo foi criado a partir de "Country" separando os países em seus continentes.
* Inclusão de Gráfico de Colunas clusterizado, mostrando as "Vendas por Segmento". No eixo X está "Segment", no eixo Y está "Soma de Sales" e no campo 'legenda' está o grupo "Segmentos agrupados" para dar destaque aos segmentos que mais performaram.
* Inclusão de "Chiclet Slicer" para selecionar os anos 2013 e 2014.
* Inclusão de botões de navegação (página anterior, próxima página, HOME).

### 05 - Página Séries Temporais
* Inclusão de Gráfico de Dispersão para apresentar o Total de Vendas por Mês. Para esse visual foram utilizadas várias tabelas:
    1. No eixo X está a medida "Outlier", que foi criada via DAX, com o código abaixo:
> 
    outlier = CALCULATE( 
    [total de vendidos],
    FILTER(
        VALUES(financials[Product]),
        COUNTROWS( FILTER(financials, [total de vendidos] >= 150)) > 0)
    )
2. No eixo Y está "Soma de Sales";
3. Na legenda está "Product";
4. No tamanho está "Soma de Sales";
5. No eixo de reprodução está "Date - Mês"
* Inclusão de outro Gráfico de Dispersão para apresentar o Total de Lucro por Mês. Esse gráfico utiliza as mesmas estruturas do gráfico anterior, apenas substituindo os campos onde há "Soma de Sales" por "Soma de Profit".
* Inclusão de Botões para alternar entre os visuais de "VENDAS" e "LUCRO" dos gráficos de dispersão.
* Inclusão de Visual Personalizado "Radar Chart" para apresentar outra maneira de ver a quantidade de vendas por produto. Esse visual não acompanha a execução do "Play" dos gráficos anteriores.
* Inclusão de Matriz para mostrar a "Vendas por Trimestre". Nas linhas estão os Trimestres, e nas colunas estão os Anos. Tanto para linhas quanto para colunas estão os Totais de Vendas.
* Inclusão de Chiclet Slicer para selecionar o Ano.
* Inclusão de Chiclet Slicer para selecionar os Meses. Ambos tem iteração com o "Radar Chart".



## OBSERVAÇÕES
1. Não achei necessário incluir mais páginas ou visuais pois acredito que seriam apenas repetições das informações apresentadas.
2. Outros visuais poderiam ser incluídos, como o "Bullet Chart" e o "Infográfic Designer", mas não há informações relevantes o suficiente que justifiquem a utilização de tais visuais.
3. Menos é mais. Quanto mais coisas dentro do gráfico, certamente a informação principal seria deixada de lado. Então, priorizei ter no máximo 4 gráficos por aba (com exceção da página principal). O que exceder a isso, que vos seja anátema.