from flask import Flask
from config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True) # from instance folder
 
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app