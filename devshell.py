from flask_sqlalchemy_booster import run_interactive_shell
from app.models import db, User, PushSubscription
from app.app_factory import create_app


app = create_app()


if __name__ == '__main__':
    run_interactive_shell(app, db)