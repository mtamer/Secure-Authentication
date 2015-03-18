import os
import datetime

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from lab01 import app, db
from lab01.models import User


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()

if __name__ == '__main__':
    manager.run()