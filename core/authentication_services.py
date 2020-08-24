import datetime
from flask_jwt_extended import create_access_token



def generate_signup_token(username):
    expires = datetime.timedelta ( days=30 )
    token = create_access_token ( username, expires_delta=expires )
    return token


    
