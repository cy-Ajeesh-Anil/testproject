import datetime

from flask import request
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity
from flask_restplus import Resource

from CRUD import check_student_by_username_password, check_student_by_username
from core import failure, success

class Login(Resource):
    def post( self ):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not check_student_by_username_password(username,password):
            return failure(message= "Bad username or password")
        student = check_student_by_username ( username )
        if not student.verified :
            return failure ( message='Your account has not been verified' )
        expires = datetime.timedelta ( hours=10 )
        token = create_access_token ( username, expires_delta=expires )
        from flask_jwt_extended import create_refresh_token
        ret = {
            'access_token': token,
            'refresh_token': create_refresh_token(identity=username)
        }
        return success(data=ret)


class RefreshTtoken(Resource):
    @jwt_refresh_token_required
    def post( self ):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        ret = {'access_token': new_token}
        return success(data=ret)
