from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user # type: ignore

# Tutorial 05 - Aula 05 Flask
# Continuando dos passos anteriores
# 15º Passo: MOSTRAR MENSAGENS DE LOGIN E LOGOUT
        # Importar a biblioteca 'flash'
        # Na função "logout" inserir a mensagem de logout
        # No arquivo login, dentro do 'block' principal, inserir a função para apresentar uma mensagem

app = Flask(__name__)
app.secret_key = "Olá" # Essa é a chave encriptada
app.permanent_session_lifetime = timedelta(seconds=45)

@app.route("/")
def home():
    return render_template("conteudo.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']


        session["user"] = user
        flash("Logando. Redirecionando ... Logado com Sucesso!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Você já está Logado.")
            return redirect("user")
        return render_template("login")
    
        #db = db.get_db()
        #error = None
        #user = db.execute(
        #    'SELECT * FROM user WHERE username = ?', (email,)
        #).fetchone()

        #if user is None:
        #    error = 'Incorrect username.'
        #elif not check_password_hash(user['password'], pwd):
        #    error = 'Incorrect password.'
        
        #if error is None:
        #    session.clear()
        #    session['user_id'] = user['id']
        #    return redirect(url_for('index.html'))

        #flash(error)
        
        #login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')

'''
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanet = True
        email = request.form["email"]
        session["user"] = user
        flash("Logando. Redirecionando ... Logado com Sucesso!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Você já está Logado.")
            return redirect("user")
        return render_template("login.html")
'''
@app.route("/logout")
def logout():
    flash("Você está saindo da página. Redirecionando ... ", "info")
    session.pop("user", None)
    return redirect(url_for("login"))



@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return redirect(url_for("index"))
    else:
        flash("Você não está logado! Redirecionando para a página... ")
        return redirect(url_for("login"))
    

@app.route("/index")
def index():
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)


# PS1: Todas as vezes que você iniciar um novo ambiente virtual, será necessário instalar o flask através do CMD: pip install flask
# PS2: para evitar a necessidade de reiniciar o terminal várias vezes após uma alteração, colocar em 'app.run()' o parâmetro 'debug=True'