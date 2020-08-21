from flask_sqlalchemy import SQLAlchemy
from settings import db
from models.enumeration_tables import Country,States,City,Language
from models.institution_tables import Institution_type,Institution,Education_level,Grading_scheme,Grade
from models.test_score_tables import Exam,Language_test,Verbal,Quantitative,Writing,Speaking,Listening,Rank,Reading,Total
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String)
    verified = db.Column(db.Boolean)
    education = relationship('Education',backref='student') #### One to many relation ship with education table

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    student = relationship("Student", backref=backref("student", uselist=False))
    photo = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    title = db.Column(db.String)
    gender = db.Column(db.String)
    address = db.Column(db.String)
    citizenship_id = db.Column(db.Integer,db.ForeignKey('country.id'))
    citizenship = relationship("Country", foreign_keys=[citizenship_id])
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    country_id = db.Column(db.Integer,db.ForeignKey('country.id'))
    country = relationship("Country", foreign_keys=[country_id])
    postal_code = db.Column(db.String)
    passport_no = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    language_id = db.Column(db.Integer,db.ForeignKey('language.id'))
    marital_status = db.Column(db.String)
    email = db.Column(db.String)
    created_on = db.Column(db.DateTime, server_default=db.func.now())

class Emergency_contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = relationship("Student", backref=backref("student", uselist=False))
    emy_name = db.Column(db.String)
    emy_phone = db.Column(db.String)
    emy_email = db.Column(db.String)
    emy_relationship = db.Column(db.String)
    emy_address = db.Column(db.String)
    created_on = db.Column(db.DateTime, server_default=db.func.now())

###### Education model
class Education(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True )
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    country_id = db.Column(db.Integer,db.ForeignKey('country.id'))
    education_level_id = db.Column(db.Integer,db.ForeignKey('education_level.id')) #### level of education
    institution_id = db.Column(db.Integer,db.ForeignKey('institution.id')) ### Board/ university
    institution_type_id = db.Column(db.Integer,db.ForeignKey('institution_type.id')) ###School type
    grading_scheme_id = db.Column(db.Integer,db.ForeignKey('grading_scheme.id')) ### Grade scheme
    grade_id = db.Column(db.Integer,db.ForeignKey('grade.id'))### Grade
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    school_name = db.Column(db.String)
    school_address = db.Column(db.String)
    student_number = db.Column(db.String)
    most_recent = db.Column(db.Boolean)
    created_on = db.Column(db.DateTime, server_default=db.func.now())


##### Test Score for exam
class Exam_test_score(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam_date = db.Column(db.Date)
    verbal_id = db.Column(db.Integer, db.ForeignKey('verbal.id'))
    verbal_rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'))
    quantitative_id = db.Column(db.Integer, db.ForeignKey('quantitative.id'))
    quantitative_rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'))
    writing_id = db.Column(db.Integer, db.ForeignKey('writing.id'))
    writing_rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'))
    total_id = db.Column(db.Integer, db.ForeignKey('total.id'))
    total_rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'))


#### Test score model for language proficiency test
class Language_test_score(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    test_id = db.Column(db.Integer, db.ForeignKey('language_test.id'))
    exam_date = db.Column(db.Date)
    listening_id = db.Column(db.Integer, db.ForeignKey('listening.id'))
    reading_id = db.Column(db.Integer, db.ForeignKey('reading.id'))
    writing_id = db.Column(db.Integer, db.ForeignKey('writing.id'))
    speaking_id = db.Column(db.Integer, db.ForeignKey('speaking.id'))