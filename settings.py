from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail, Message

app = Flask(__name__, template_folder="templates")

### Environment variables from .env file

db_username=os.environ.get('DB_USERNAME')
db_password=os.environ.get('DB_PASSWORD')
host=os.environ.get('HOST')
port=os.environ.get('PORT')
db_name=os.environ.get('DB_NAME')

DB_CONNECTION_STRING = 'postgresql://'+str(db_username)+':'+str(db_password)+'@'+str(host)+':'+str(port)+'/'+str(db_name)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'arunyajayan@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'arunyajayan@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'arunyajayan123#' # mail password


app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
migrate = Migrate(app,db)
mail = Mail(app)