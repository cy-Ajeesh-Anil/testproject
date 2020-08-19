from flask_restplus import Namespace, Resource, fields
from models.student import Student
from settings import db
from core import failure, success, send_mail

api = Namespace('students', description='Student related operations')
student = api.model('Student', {
    'id': fields.String(required=True, description='The cat identifier'),
    'username': fields.String(required=True, description='The cat name'),
})
class Signup ( Resource ) :

	def post (self) :
		from flask import request
		request = request.json
		import re;
		if not('username' in request):
			return failure(message='username field missing')
		if not('password' in request):
			return failure(message='password field missing')
		if request['username'].strip()=='':
			return failure(message='Invalid email')
		if request['password'].strip()=='':
			return failure(message='Invalid password')
		if not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", request['username'].strip())):
		# if(re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',request['username'])):
			return failure(message='Invalid email')
		if db.session.query(Student).filter_by(username=request['username'].strip()).first():
			return failure(message='Email already registered')
		student = Student(verified=False,username=request['username'].strip(),password=request['password'].strip())
		db.session.add(student)
		db.session.commit()
		student = db.session.query(Student).filter_by(username=request['username'].strip()).first()
		send_mail(recipients=student.username)
		return success(data= {'id':student.id,'username':student.username},message='Your verificaton mail has been sent')
