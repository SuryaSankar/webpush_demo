from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db
from app.app_factory import create_app


def run_migrations():

    manager = Manager(create_app)
    manager.add_command('db', MigrateCommand)
    manager.add_option('--callback', dest='callback', default=Migrate)
    manager.add_option('--callback-args', dest='callback_args',
                       default=[db])

    manager.run()


if __name__ == '__main__':
    run_migrations()
