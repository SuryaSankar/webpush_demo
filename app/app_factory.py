from flask import Flask
from .views import main_pages_bp, main_api_bp, admin_pages_bp, admin_api_bp
from .models.core import db
from .models.user import user_datastore
from flask_security import Security


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config')

    # Create a folder called instance and create a file called
    # application.cfg.py there. You can add config variables which 
    # should not be version committed there
    app.config.from_pyfile('application.cfg.py')

    db.init_app(app)
    Security(app, user_datastore)

    app.register_blueprint(main_pages_bp)
    app.register_blueprint(main_api_bp, url_prefix="/api")
    app.register_blueprint(admin_pages_bp, url_prefix="/admin")
    app.register_blueprint(admin_api_bp, url_prefix="/admin-api")

    return app
