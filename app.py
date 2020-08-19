from flask import Flask
from settings import app,mail
from apis import api
from models import *
from flask import Flask,request,jsonify,render_template
from apis import Signup

# app = Flask(__name__)
api.init_app(app)
api.add_resource ( Signup, '/signup' )

if __name__ == '__main__':
    app.run(debug=False)
