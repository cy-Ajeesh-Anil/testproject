from flask_sqlalchemy import SQLAlchemy
from settings import db
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

### Country table
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String)
    country_code = db.Column(db.String)
    states = relationship("States",back_populates="country")

#### states table, different states under different countries
class States(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    state_name = db.Column(db.String)
    country_id = db.Column(db.Integer,db.ForeignKey('country.id'))
    country = relationship("Country", back_populates="states")
    city = relationship("City",back_populates="states")

#### city table, different cities under different states
class City(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    city_name = db.Column(db.String)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    states = relationship("States",back_populates="city")
### Table for different languages
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language = db.Column(db.String)
