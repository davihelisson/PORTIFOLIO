from flask import Flask, redirect, url_for

# Tutorial 01 - Aula 01 Flask
# 1º Passo: importar o flask na primeira linha do arquivo .py
# 2º Passo: Criar uma instãncia para aplicação Web
app = Flask(__name__)

# 4º Passo: Colocar a página que você quer na WEB através de uma função
# 5º Passo: definir COMO vamos acessar essa página criada. Para isso, vamos decorar a função com uma rota "@app.route".
            # entre os parênteses vem o caminho para chegar na função. Se estiver vazio, vai direto para a página principal
@app.route("/")
def home():
    return "<h1>Hello!</h1><br> This is the main page using Flask Framework"

# 6º Passo: coloque o app para rodar através do CMD >> 'python Nome_arquivo.py"
# 7º Passo: Crie mais uma página. Nos parênteses de '@app.route' coloque "/< Alguma coisa>"
            # Esse 'alguma coisa' é o parâmetro que será substituído pelo que o usuário digitar na barra de "URL"
            # Exemplo: Se  digitar http://127.0.0.1:5000/home --> a mensagem retornará "Hello, home!"
@app.route("/<name>")
def user(name):
    return f'Hello, {name}!'


# 8º Passo: redirecionar páginas.
        # importar bibliotecas 'redirect', 'url_for' Essas bibliotecas vão me permitir redirecionar para outra função/página
        # Toda vez que o usuário digitar '/admin' na barra de URL, ele retornará para a função/página 'home'
        # Mas para que não haja conflito e erro na página em casos do usuário digitar alguma coisa que seja igual ao admin,
        # podemos refazer o redirecionamento da seguinte maneira: "return redirect(url_for("user", name="Admin"))"
        # Dessa forma, o usuário vai digitar 'admin' e o programa vai interpretar como uma palavra, impedindo de acessar outra página.
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

# 3º Passo: Colocar o app para executar. Essa linha vai ficar por ultimo no código.
if __name__ == "__main__":
    app.run()


# PS: Todas as vezes que você iniciar um novo ambiente virtual, será necessário instalar o flask através do CMD: pip install flask