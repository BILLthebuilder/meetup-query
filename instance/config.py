import os 
class Config(object):
    """Main/default configuration class."""
    DEBUG = False
    SECRET = os.getenv('SECRET') 
    DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configs for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configs for Testing"""
    TESTING = True
    DATABASE_URI = 'testing URL for the test DB'
    DEBUG = True

class StagingConfig(Config):
    """Configs for Staging"""
    DEBUG = True
    
class ProductionConfig(Config):
    """Configs for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}