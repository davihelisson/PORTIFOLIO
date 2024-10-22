from flask import Flask, redirect, url_for, render_template, request

# Tutorial 04 - Aula 04 Flask
# Continuando dos passos anteriores
# 13º Passo: MÉTODOS GET/POST
    # Criar uma função para login. Declarar no decorador os métodos POST e GET
    # Criar uma função para redirecionar à uma página que vai receber os dados do login
    # importar 'request' para alterar os métodos
    # colocar a lógica IF/ELSE na função login: Se o método requisitado for "POST", redirecionar para a página 'user'.
    # Caso contrário vai permanecer na mesma página

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("conteudo.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Olá, {usr}! <br>Seja Bem vindo a LaLaLand!</h1>"


if __name__ == "__main__":
    app.run(debug=True)


# PS1: Todas as vezes que você iniciar um novo ambiente virtual, será necessário instalar o flask através do CMD: pip install flask
# PS2: para evitar a necessidade de reiniciar o terminal várias vezes após uma alteração, colocar em 'app.run()' o parâmetro 'debug=True'