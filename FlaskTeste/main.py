from flask import flash, render_template, request, redirect, session, url_for # type: ignore
from app import app
from app.models import User
from flask_login import login_user, logout_user # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form.get['name']
        email = request.form.get['email']
        pwd = request.form.get['password']
        db = db.get_db()
        error = None

        if not name:
            error = 'Username is required.'
        elif not pwd:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, email, password) VALUES (?, ?, ?)",
                    (name, email, generate_password_hash(pwd)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {name} is already registered."
            else:
                return redirect(url_for('login.html'))

        flash(error)

    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get['email']
        pwd = request.form.get['password']

        db = db.get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], pwd):
            error = 'Incorrect password.'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)
        
        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('login'))


if __name__ in "__main__":
    app.run(debug=True)
