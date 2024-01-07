from config import BaseConfig
import os

class DevelopmentConfig(BaseConfig):
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'development_secret_key')
    DEBUG = True
    TEST = False

class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'production_secret_key')
    DEBUG = False
    TEST = False