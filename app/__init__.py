from flask import Flask
from config.config import Config
from extensions import configure_extentions
from dotenv import load_dotenv
import os
from config import FactoryConfig

def create_app():
    load_dotenv()

    app = Flask(__name__)

    env =  os.getenv('FLASK_ENV', 'development')
    config_class = FactoryConfig.get_config(env)
    print(config_class)
    app.config.from_object(config_class)

    @app.route('/')
    def hello():
        return '<h2>Hello World</h2>'
    
    return app