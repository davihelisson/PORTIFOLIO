
# DESAFIO DE PROJETO

## Módulo 06 - Gerenciamento de Workspaces e Datasets com Power BI

O arquivo '.pbix' é o arquvivo de Power BI contendo as modificações do dash original. As modificações estão apresentadas abaixo de acordo com a página.

### 01 - Página Parâmetros
* Duplicação da página Séreies Temporais
* Remoção dos visuais, mantendo apenas a seção de "Cabeçalho", alterando o título para "Another Details"
* Inclusão de Medidas "AVG Price", "AVG Sales", "Total Profit", "Total Discounts", Total Unit Sold", "Total Sales". A sintaxe DAX está descrita abaixo:

>
    AVG Price = AVERAGEX(financials, financials[Sale Price])

    AVG Sales = AVERAGEX(financials, financials[ Sales])

    Total Discounts = SUMX(financials, financials[Discounts])

    Total Profit = SUMX(financials, financials[Profit])

    total sales = SUMX(financials, financials[ Sales]) 

    Total Unit Sold = SUMX(financials, financials[Units Sold])
<

* Inclusão de Parâmetros com as medidas criadas nos campos.
* Inclusão de novo Parâmetro com os campos "Country", "Product" e "Segmente".
* Ambos os parâmetros foram dispostos em uma única coluna e uma única linha, respectivamente.
* Inclusão de gráfico de barras clusterizado. No eixo Y está o parâmetro "Country Product Segment", e no eixo X estão os parâmetros de totais de AVG criados anteriormente.
* Inclusão de Visual Personalisado "Infographic Designer 1.9.7". Na campo "Category" está o parâmetro "Country Product Segment" e no campo "Measure" está a Soma de Profit
* Inclusão de Visual Personalisado Radar Chart. Na categoria está "Product" e no eixo está o parâmetro de Totais e AVG.



OBS:

1) As medidas tiveram que ser criadas pois a linguagem DAX não permite que sejam usadas as tabelas para fazer as operações.
2) O gráfico de barras clusterizado foi criado usando ambos os parâmetros para facilitar a comparação de acordo com a seleção do botão de parâmetro.
3) A ideia do Visual "Infographic" é mostrar exclusivamente o lucro de acordo com os parâmetros "Country Product Segment". 
4) A ideia do Visual "Radar" é mostrar os totais e médias de acordo com o produto. CUIDADO: selecionar mais de um parâmetro pode prejudicar a visualização dos dados por causa das diferentes escalas de valores.
