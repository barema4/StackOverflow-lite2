"""
   Module for for defining the configurations
"""  
class Config(object):
    """
       Method for defining the default environment
    """  
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'kalyango'

class DevelopmentConfig(Config):
    """
       Method for defining the development environment
    """   
    DEBUG = True
    TESTING = True
    ENV = "development"
    SECRET_KEY = 'kalyango'
    
    