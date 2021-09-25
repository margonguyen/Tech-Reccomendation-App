"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_MONGO_URI')
    DATABASE_PASS = environ.get('PROD_MONGO_PASS')
    DATABASE_PORT = environ.get('PROD_MONGO_PORT')



class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_NAME = 'test-mongo'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '27017'