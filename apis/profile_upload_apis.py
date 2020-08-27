from models import Profile
from flask_restplus import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from CRUD import check_student_by_username, create_student, verify_student,upload_profile,update_profile_image
from core import failure, success
import os
from uuid import uuid4
from settings import db
from flask import request



class ProfileImageUpdate(Resource):
    @jwt_required
    def put(self):
        current_user = get_jwt_identity()
        # print(current_user)
        student = check_student_by_username(current_user)
        # print(student.id)
        profile = db.session.query(Profile).filter_by(student_id=student.id).first()
        print(profile.student_id)

        if 'image' in request.files:
            file = request.files['image']
            profile_image = upload_profile(file)
            print(profile_image)
            update_image = update_profile_image(profile_image,student_id=profile.student_id)
            if update_image:
                return success(message="Profile image uploaded successfully")
            return failure("Unable to upload")
        return failure("Please upload an image")




