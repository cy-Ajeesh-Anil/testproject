
class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DB_CONNECTION_STRING = 'postgres://xyprrcsjrxrkdg:73c9a26fba53de293f10f965a9443f270c23c29c1c390b8c49b208ef3bc19712@ec2-54-144-177-189.compute-1.amazonaws.com:5432/d464ivfc7vnh1g'
    FRONT_END_URL = 'https://qa-inscholaris-web-student.herokuapp.com/#/'
    BACK_END_URL = 'https://qa-inscholaris-api.herokuapp.com/'
    DEBUG = True

class DevelopmentConfig(Config):
    DB_CONNECTION_STRING = 'postgres://vntugecoaypdwx:f6f2e2061bd82e591f8ff63892499b0b8fb1ea0c0c9afa89b7a51ed7685e49f0@ec2-3-217-87-84.compute-1.amazonaws.com:5432/d1a958r4jes78'
    FRONT_END_URL = 'https://dev-inscholaris-web-student.herokuapp.com/#/'
    BACK_END_URL = 'https://dev-inscholaris-api.herokuapp.com/'
    DEBUG = True
class LocalDevelopmentConfig(Config):
    DB_CONNECTION_STRING = 'postgresql://postgres:postgres@localhost:5433/inscholaris'
    # FRONT_END_URL = 'https://dev-inscholaris-web-student.herokuapp.com/#/'
    # BACK_END_URL = 'https://dev-inscholaris-api.herokuapp.com/'
    DEBUG = True