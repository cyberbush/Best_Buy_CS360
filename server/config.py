import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bestbuy.db'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    DEBUG = True
    CSRF_ENABLED = True