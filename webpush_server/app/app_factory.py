from flask_sqlalchemy_booster import FlaskBooster
from .views import main_bp, api_bp
from .models.core import db
from .models.user import user_datastore
from flask_security import Security

security = Security()


def create_app(callback=None, callback_args=[], callback_kwargs={}):
    app = FlaskBooster(__name__)
    app.config.from_object('app.config')

    db.init_app(app)
    security.init_app(app, user_datastore)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    if callback is not None:
        callback(app, *callback_args, **callback_kwargs)
    return app
