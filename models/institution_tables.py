from flask_sqlalchemy import SQLAlchemy
from settings import db
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from models.enumeration_tables import Country,States,City,Language

### Education levels representing table (level of education)
class Education_level(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

### institution types representing table
class Institution_type(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

### institutions representing table(boadr/university)
class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    institution_type_id = db.Column(db.Integer, db.ForeignKey('institution_type.id'))

class Grading_scheme(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scheme = db.Column(db.String)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade = db.Column(db.String)
    grade_scheme_id = db.Column(db.Integer, db.ForeignKey('grading_scheme.id'))
