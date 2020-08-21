from settings import db
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref


### Table for storing diffrent exams
class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exam_name = db.Column(db.String(50))


###### Table for storing different language proficiency test
class Language_test(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    test_name = db.Column(db.String(50))

#### Table for storing verbal scores
class Verbal(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    score = db.Column(db.Float)

#### Table for storing quantitative scores
class Quantitative(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Float)

#### Table for storing writing score of exams
class Writing(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Float)

#### Table for storing total scores of exams
class Total(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Float)

#### Table for storing listening scores of exams
class Listening(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Float)

#### Table for storing reading scores of exams
class Reading(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Float)

#### Table for storing speaking scores of exams
class Speaking(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Float)

#### Table for storing Rank persentage of exams
class Rank(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    rank_percentage = db.Column(db.Integer)


