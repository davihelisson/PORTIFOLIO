import csv
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "secret"
# Configurando o Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configurando o armazenamento temporário de login
app.permanent_session_lifetime = timedelta(minutes=1)
with app.app_context():


    # Instanciando o bd
    db = SQLAlchemy(app)


    # Criando uma classe para criar o bd
    class users(db.Model):
        _id = db.Column("id", db.Integer, primary_key=True)
        fname = db.Column("name", db.String(100))
        lname = db.Column("lastname", db.String(100))
        email = db.Column("email", db.String(100))

        def __init__(self, fname, email):
            self.fname = fname
            self.email = email


    @app.route("/")
    def home():
        return render_template("index.html")


    # Aqui vamos fazer uma página para vizualizar os dados salvos
    @app.route("/view")
    def view():
        values = users.query.all()
        return render_template("view.html", values=values)


    # Aqui definido o login
    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            session.permanent = True
            user = request.form["name"]
            session["user"] = user

            found_user = users.query.filter_by(fname=user).first()

            if found_user:
                session["email"] = found_user.email
            else:
                email = request.form["email"]
                usr = users(user, email)
                db.session.add(usr)
                db.session.commit()

            flash("Login Successful!.")
            return redirect(url_for("user"))
        else:
            if "user" in session:
                flash("Already Logged In!")
                return redirect(url_for("user"))

        return render_template("login.html")


    # Aqui está definido o logout
    @app.route("/logout")
    def logout():
        if "user" in session:
            user = session["user"]
            flash("You have been logedd out.", "info")
        session.pop("user", None)
        session.pop("email", None)
        return redirect(url_for("login"))


    # Aqui vai ser o que fazer quando logar
    @app.route("/user", methods=["POST", "GET"])
    def user():
        email = None
        if "user" in session:
            user = session["user"]

            if request.method == "POST":
                email = request.form["email"]
                session["email"] = email

                found_user = users.query.filter_by(email=email).first()
                found_user.email = email
                db.session.commit()
                flash("Email was saved!")
            else:
                if "email" in session:
                    email = session["email"]
            
            return render_template("user.html", email=email)
        else:
            flash("You are not logged yet.")
            return redirect(url_for("login"))

# Aqui é o comando para apagar os dados
    @app.route("/deletardb")
    def deletardb():
        db.drop_all()
        return redirect(url_for("home"))


# Aqui é o comando para fazer backup dos dados em um arquivo ".CSV"
    @app.route("/backupdb")
    def backup_db():
        with open('backup.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Escrevendo o cabeçalho
            csvwriter.writerow(['name', 'email'])

            # Escrevendo os dados
            for row in users.query.all():
                csvwriter.writerow([row.fname, row.email])

        return redirect(url_for("home"))



    if __name__ == "__main__":
        db.create_all()
        app.run(debug=True)