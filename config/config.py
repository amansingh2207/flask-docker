import os

class Config:
    #all global settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'some_database_url')

class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG', True)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'some_database_url')

class ProductionConfig(Config):
    DEBUG = os.environ.get('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'some_database_url')

class TestConfig(Config):
    DEBUG = os.environ.get('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'some_database_url')

