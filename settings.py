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
DB_CONNECTION_STRING = 'postgres://vntugecoaypdwx:f6f2e2061bd82e591f8ff63892499b0b8fb1ea0c0c9afa89b7a51ed7685e49f0@ec2-3-217-87-84.compute-1.amazonaws.com:5432/d1a958r4jes78'
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
