import os

class Config(object):
    SECRET_KEY = 'itconsultants_2020_proyecto_Voxcall'
    MAIL_SERVER: 'smtp.gmail.com'
    MAIL_PORT: 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dtapia@itconsultants.cl'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')

class DevelopmentConfig (Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/voxcall'
    SQLALCHEMY_TRACK_MODIFICATIONS = False