from core import generate_signup_token, send_mail
from models import Student,Profile
from settings import db,app
import os
from uuid import uuid4

def upload_profile(file):
    extension = os.path.splitext(file.filename)[1]
    f_name = str(uuid4()) + extension
    path = os.path.join(app.config['UPLOAD_FOLDER'], f_name)
    file.save(path)
    if path:
        return path
    return None

def update_profile_image(profile_image,student_id):
    profile = db.session.query(Profile).filter_by(student_id=student_id).update(dict(photo=profile_image))
    db.session.commit ( )
    if profile:
        return profile
    return None

