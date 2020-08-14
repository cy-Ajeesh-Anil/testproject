from flask_sqlalchemy import SQLAlchemy
from settings import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String)
    verified = db.Column(db.Boolean)