import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # simplemde conf
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    # db conf
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cephas:admin121@localhost/flask_blog'

    UPLOADED_PHOTOS_DEST ='app/static/images/blog'
    
    @staticmethod
    def init_app(app):
        pass

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