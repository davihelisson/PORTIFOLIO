from flask import Flask, redirect, url_for, render_template

# Tutorial 01 - Aula 02 Flask
# 1º Passo: importar o flask na primeira linha do arquivo .py
# 2º Passo: Criar uma instãncia para aplicação Web
# 3º Passo: Colocar o app para executar. Essa linha vai ficar por ultimo no código.
# 4º Passo: Colocar a página que você quer na WEB através de uma função
# 5º Passo: definir COMO vamos acessar essa página criada. Para isso, vamos decorar a função com uma rota "@app.route".
            # entre os parênteses vem o caminho para chegar na função. Se estiver vazio, vai direto para a página principal
# 6º Passo: coloque o app para rodar através do CMD >> 'python Nome_arquivo.py"
# 7º Passo: Crie mais uma página. Nos parênteses de '@app.route' coloque "/< Alguma coisa>"
            # Esse 'alguma coisa' é o parâmetro que será substituído pelo que o usuário digitar na barra de "URL"
            # Exemplo: Se  digitar http://127.0.0.1:5000/home --> a mensagem retornará "Hello, home!"
# 8º Passo: redirecionar páginas.
        # importar bibliotecas 'redirect', 'url_for' Essas bibliotecas vão me permitir redirecionar para outra função/página
        # Toda vez que o usuário digitar '/admin' na barra de URL, ele retornará para a função/página 'home'
        # Mas para que não haja conflito e erro na página em casos do usuário digitar alguma coisa que seja igual ao admin,
        # podemos refazer o redirecionamento da seguinte maneira: "return redirect(url_for("user", name="Admin"))"
        # Dessa forma, o usuário vai digitar 'admin' e o programa vai interpretar como uma palavra, impedindo de acessar outra página.
# 9º Passo: Fazer TEMPLATES:
        # Importar 'render_template' na primeira linha.
        # A função irá permitir que peguemos uma página HTML e renderizar como uma nossa página WEB
        # Crie uma pasta chamada 'Templates' na mesma pasta do arquivo que será executado.
        # Crie uma arquivo HTML e salve dentro da pasta 'Templates'
        # Substitua o return da página para o 'render_template' e nos parênteses coloque o nome da página que você quer exibir "index.home"
# 10º Passo: Informações dinâmicas na página:
        # Como eu faria para aparecer o nme do usuário na página inicial: 
        # em @app.route() coloque entre aspas a tag "/<name>" e 'name' como argumento da função.
        # No arquivo HTML, as funções terão que ser escritas entre dois colchetes {{desse jeito aqui}}
        # No return após o nome da página, inserir 'content=name' --> Dessa forma o que o usuário digitar no buscador, vai aparecer lá no HTML
            # A página sem nada no buscador aparecerá como um "NOT FOUND PAGE"
# 11º Passo: implementar código Python diretamente no arquivo HTML
        # Ao invés de dois colchetes, colocamos {% conteudo %}


app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, content1=["Davi", "Aline", "Eduardo", "Jorge"])



if __name__ == "__main__":
    app.run()


# PS: Todas as vezes que você iniciar um novo ambiente virtual, será necessário instalar o flask através do CMD: pip install flask