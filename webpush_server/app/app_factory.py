from flask import Flask
from .views import main_bp, api_bp
from .models.core import db


def create_app(callback=None, callback_args=[], callback_kwargs={}):
    app = Flask(__name__)
    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    if callback is not None:
        callback(app, *callback_args, **callback_kwargs)
    return app
