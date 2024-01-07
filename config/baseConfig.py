from abc import ABC, abstractclassmethod

class BaseConfig(ABC):
    # Define mandatory properties/methods that all configurations must have
    @property
    @abstractclassmethod
    def SECRET_KEY(self):
        pass

    DEBUG = True
    TEST = True