import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # simplemde conf
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    # db conf
    SQLALCHEMY_TRACK_MODIFICATIONS = False


        # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    UPLOADED_PHOTOS_DEST ='app/static/images/blog'
    
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cephas:admin121@localhost/flask_blog'

class TestConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    DEBUG=False


config_loader = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}