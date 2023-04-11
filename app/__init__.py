import os
from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

# Create Flask app instance
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    csrf = CSRFProtect(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # Set up upload folder
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

    # Import views
    from app import views

    return app

app = create_app()
