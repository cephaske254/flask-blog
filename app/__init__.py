from flask import Flask
from config import Config,config_loader
def create_app(conf_type):
    app = Flask(__name__)

    # COFIGURATIONS
    app.config.from_object(Config)
    app.config.from_object(config_loader[conf_type])
    
    return app