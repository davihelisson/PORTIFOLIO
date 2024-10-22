from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader # type: ignore
def get_user(user_id):
    return User.get(user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(90), nullabel=False)
    email = db.Column(db.String(90), nullabel=False, unique=True)
    password = db.Column(db.String(128), nullabel=False)

def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = generate_password_hash(password)

def veritfy_password(self, pwd):
    return check_password_hash(self.passwprd, pwd)


