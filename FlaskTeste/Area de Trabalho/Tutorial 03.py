from flask import Flask, redirect, url_for, render_template

# Tutorial 01 - Aula 03 Flask
# Continuando dos passos anteriores
# 12º Passo: Criar um arquivo 'Base' para colocar o HTML padrão
        # Crie também outra página onde o conteúdo será alterado. Essa página é que será acessada pelo Python

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("conteudo.html", content="Testando...")



if __name__ == "__main__":
    app.run(debug=True)


# PS1: Todas as vezes que você iniciar um novo ambiente virtual, será necessário instalar o flask através do CMD: pip install flask
# PS2: para evitar a necessidade de reiniciar o terminal várias vezes após uma alteração, colocar em 'app.run()' o parâmetro 'debug=True'