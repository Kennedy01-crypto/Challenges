from flask import Flask
from config import Config
import os

def create_app(config_Class = Config):
    app = Flask(__name__, instance_relative_config=True)

    # load configuration
    app.confug.from_object(config_Class)
    app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register blueprints, extensions, etc
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app