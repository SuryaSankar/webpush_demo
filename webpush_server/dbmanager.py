from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db
from app.app_factory import create_app


def create_db_manager():
    app = create_app()
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager


if __name__ == '__main__':
    create_db_manager().run()
