from config import DevelopmentConfig, ProductionConfig

class FactoryConfig:
    @staticmethod
    def get_config(env=None):
        if env == 'development':
            return DevelopmentConfig
        elif env == 'production':
            return ProductionConfig
        else:
            raise Exception('Invalid environment. Please check env file')