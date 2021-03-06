from flask import Flask
import datetime
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_marshmallow import Marshmallow




app = Flask(__name__, template_folder="templates")

if app.config['ENV']=='production':
	app.config.from_object("config.ProductionConfig")
if app.config['ENV']=='development':
	app.config.from_object("config.DevelopmentConfig")
if app.config['ENV']=='localdevelopment':
	app.config.from_object("config.LocalDevelopmentConfig")



app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_CONNECTION_STRING']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
migrate = Migrate(app,db)
marshmallow = Marshmallow(app)

#mail server configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'test.inscholaris@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'test.inscholaris@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'cycloides@123!' # mail password
mail = Mail(app)

##Profile upload folder
UPLOAD_FOLDER = 'students_uploads/profile'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#Authentication config
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=5)
app.config['JWT_SECRET_KEY'] = 'P)O(I*U&Y^T%R$E#W@Q!AWSEDRFTGYHUJIKOLP;{"?>L<KMJNHBGVFCDXSZAzxCVcvBNbnM,<>>?'  # Change this!
jwt = JWTManager(app)


