from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

# Tutorial 05 - Aula 05 Flask
# Continuando dos passos anteriores
# 14º Passo: CRIAR SESSÕES (PARA ARMAZENAR O LOGINS)
    # Importar 'session'. As sessões serão configuradas com base no que o usuário inserir no login
    # Inserir na função 'login' a session para uma 'lista de usuários'.
    # Na função 'user', coloque uma condição para verificar se há alguma informação na session. Caso contrário, retornar para a página de login.
    # Crie uma chave encriptada
    # Criar uma função de 'logout' para poder apagar as informações
    # Criar um tempo de salvamento do login, mesmo que a página seja fechada


app = Flask(__name__)
app.secret_key = "Olá" # Essa é a chave encriptada
app.permanent_session_lifetime = timedelta(seconds=30)

@app.route("/")
def home():
    return render_template("conteudo.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanet = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:             # Se o usuário já estiver logado, redirecionar para a página User
            return redirect("user")
        return render_template("login.html") # Caso contrário, vá para a página de login

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



@app.route("/user")
def user():
    if "user" in session:               # Verificando se o valor inserido existe na lista de usuários cadastrados no login
        user = session["user"]
        return redirect(url_for("index"))
    else:                              # Se não existir, vai direcionar para a página de login
        return redirect(url_for("login"))
    

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


# PS1: Todas as vezes que você iniciar um novo ambiente virtual, será necessário instalar o flask através do CMD: pip install flask
# PS2: para evitar a necessidade de reiniciar o terminal várias vezes após uma alteração, colocar em 'app.run()' o parâmetro 'debug=True'