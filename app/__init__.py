from flask import Flask
from config import Config,config_loader
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy

simplemde = SimpleMDE()
db = SQLAlchemy()
def create_app(conf_type):
    app = Flask(__name__)


    # COFIGURATIONS
    app.config.from_object(config_loader[conf_type])
    app.config.from_object(Config)


    # BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint,url_prefix='/blog')
    

    # EXTENSIONS
    simplemde.init_app(app)
    db.init_app(app)
    
    return app