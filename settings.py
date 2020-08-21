from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail

app = Flask(__name__, template_folder="templates")

### Environment variables from .env file

db_username=os.environ.get('DB_USERNAME')
db_password=os.environ.get('DB_PASSWORD')
host=os.environ.get('HOST')
port=os.environ.get('PORT')
db_name=os.environ.get('DB_NAME')
## DB connection
DB_CONNECTION_STRING = 'postgres://xyprrcsjrxrkdg:73c9a26fba53de293f10f965a9443f270c23c29c1c390b8c49b208ef3bc19712@ec2-54-144-177-189.compute-1.amazonaws.com:5432/d464ivfc7vnh1g'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
migrate = Migrate(app,db)


#mail server configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'test.inscholaris@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'test.inscholaris@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'cycloides@123!' # mail password
mail = Mail(app)
