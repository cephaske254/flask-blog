import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True

class TestConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    DEBUG=False


config_loader = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}