from . import db
from flask_login import UserMixin
#from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
    passwords = db.relationship('Password', backref='owner', lazy=True)


class Password(db.Model):
    __tablename__ = 'passwords'
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(150), nullable=False)
    site_url = db.Column(db.String(300), nullable=True)
    site_password = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
