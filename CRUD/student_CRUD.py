from core import generate_signup_token, send_mail
from models import Student
from settings import db


def check_student_by_username ( username=None,verified=None ) :
	student = db.session.query ( Student ).filter_by ( username=username ).first ( )
	if student :
		return student
	return None

def check_student_by_username_password( username,password):
	student=db.session.query(Student).filter_by(username=username,password=password,verified=True).first()
	if student :
		return student
	return None

def create_student ( username=None, password=None ) :
	student = Student ( verified=False, username=username,
	                    password=password )
	db.session.add ( student )
	db.session.commit ( )
	if bool ( check_student_by_username ( username ) ) :
		token = generate_signup_token(username)
		send_mail ( recipients=student.username,token=token )
		return check_student_by_username ( username )
	return None

def verify_student(student):
	student.verified=True
	db.session.commit()

def serialize ( students ) :
	data = [ ]
	for student in students :
		dict = {}
		dict [ 'id' ] = student.id,
		dict [ 'username' ] = student.username
		data.append ( dict )
	return data

