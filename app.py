from flask import Flask
from settings import app
from apis import api
from models import *


# app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=False)
