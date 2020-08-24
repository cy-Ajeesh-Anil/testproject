from flask_restplus import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from CRUD import check_student_by_username, create_student, verify_student
from core import failure, success

class Signup ( Resource ) :
	def post (self) :
		from flask import request
		request = request.json
		if request==None:
			return failure(message='Bad request body')
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
		if check_student_by_username(username=request['username'].strip()):
			return failure(message='Email already registered')
		create_student(username=request['username'].strip(),password=request['password'].strip())
		student = check_student_by_username(username=request['username'].strip())
		return success(data= {'id':student.id,'username':student.username},message='Your verificaton mail has been sent')
	
class VerifyStudent(Resource):
	@jwt_required
	def put( self ):
		current_user = get_jwt_identity ( )
		student = check_student_by_username(current_user)
		if student.verified :
			return success(message='Your account has been already verified')
		verify_student(student=student)
		return success(data=current_user,message='Successfully verified')