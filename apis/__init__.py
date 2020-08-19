from flask_restplus import Api
from .Cat import api as ns1
from .student_api import Signup
api = Api(
    title='InScholaris API',
    version='1.0',
    description='InScholaris api description',
    # All API metadatas
)

api.add_namespace(ns1)

