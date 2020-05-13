from flask import Flask
from config import Config,config_loader
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'

simplemde = SimpleMDE()
db = SQLAlchemy()
mail = Mail()
def create_app(conf_type):
    app = Flask(__name__)

    # COFIGURATIONS
    app.config.from_object(config_loader[conf_type])
    app.config.from_object(Config)

    # confg upload set
    configure_uploads(app,photos)

    # BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)
        

    # EXTENSIONS
    simplemde.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    return app