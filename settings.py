from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

### Environment variables from .env file

db_username=os.environ.get('DB_USERNAME')
db_password=os.environ.get('DB_PASSWORD')
host=os.environ.get('HOST')
port=os.environ.get('PORT')
db_name=os.environ.get('DB_NAME')

DB_CONNECTION_STRING = 'postgresql://'+str(db_username)+':'+str(db_password)+'@'+str(host)+':'+str(port)+'/'+str(db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
migrate = Migrate(app,db)