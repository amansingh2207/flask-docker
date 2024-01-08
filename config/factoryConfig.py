from app.utils.logger_factory import configure_logger
from config import DevelopmentConfig, ProductionConfig

class FactoryConfig:
    @staticmethod
    def get_config(env=None):
        if env == 'development':
            return DevelopmentConfig
        elif env == 'production':
            return ProductionConfig
        else:
            logger = configure_logger("FactoryConfig")
            logger.error('Invalid environment')
            raise Exception('Invalid environment. Please check env file')