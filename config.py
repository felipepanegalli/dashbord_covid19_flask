import os


class Config:
    CSRF_ENABLE = True
    SECRET = 'nf9sdn8fys9df020fy3fnwef923y39fy23f79wneyf9f8nywef09yw'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.ROOT_DIR, 'db.sqlite3')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '192.0.0.1'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'
