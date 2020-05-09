from flask import Flask
from config import Config,config_loader
def create_app(conf_type):
    app = Flask(__name__)

    # COFIGURATIONS
    app.config.from_object(Config)
    app.config.from_object(config_loader[conf_type])

    # BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint,url_prefix='/blog')
    
    return app