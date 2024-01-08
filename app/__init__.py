import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import configure_extentions
from config import FactoryConfig
from .utils.logger_factory import configure_logger


def create_app():
    load_dotenv()

    app = Flask(__name__)

    env =  os.getenv('FLASK_ENV', 'development')
    config_class = FactoryConfig.get_config(env)
    print(config_class)
    app.config.from_object(config_class)

    # Initialize extensions
    configure_extentions(__name__)

    #Configure logger
    logger = configure_logger("Splitzer")
    logger.info("Starting app...")

    @app.route('/')
    def hello():
        return '<h2>Hello World</h2>'
    
    return app