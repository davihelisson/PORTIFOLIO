
# DESAFIO DE PROJETO
## Modelagem e transformação de dados com DAX no Power BI




## Autores

- [@davihelisson](https://www.github.com/davihelisson)


## Processo de Construção

### I - Criação de tabelas

* Duplicação de tabelas a partir da tabela 'Financials Sample'
* Renomear as tabelas colocando um prefixo "D_" para as tabelas dimensão e "F_" para a tabela fato.
"""

    D_Produtos (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)

    D_Produtos_Detalhes (ID_produto, Discount Band, Sale Price,  Units Sold, Manufactoring Price)

    D_Descontos (ID_produto, Product, Discount, Discount Band)

    D_Detalhes (ID_produto, Product, Segment, Country, Sales, Gross Sales, COGS, Profit, Date)
    
    D_Categoria (Índice, Segment, Country)

-->> A tabela 'D_Produto' foi criada pela agurpamento (Botão de "Agrupar por", na guita "Transformar" dentro do editor do Power Query) de acordo com os critérios descritos acima.

* A tabela "F_VENDA" é a tabela fato, e possui os seguintes campos:
"""

    F_Vendas (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount  Band, Segment, Country, Salers, Profit, Date (campos))


### II -Funções DAX 

As funções DAX utilizadas para a construção da tabela de DATAS foram:
* **SELECTCOLUNMS** - Para selecionar uma coluna de outra tabela, referenciada no início da sintaxe para criação da tabela.
* **YEAR** - Para retornar o ano de uma coluna de data
* **MONTH** - Para retornar o mês (numeral) de uma coluna de data.
* **QUARTER** - Para retornar o numero do trimestre (de 01 a 04) de uma coluna de data.
* **WEEKNUM** - Para retornar o número da semana de uma coluna de data.

_OBS:_ Caso queria colocar o mês por extenso, recomendo inserir uma nova coluna e formatar com pela função **FORMAT** e especificar a língua-país.