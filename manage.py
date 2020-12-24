import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "development")

manager = Manager(app)
# migrate = Migrate(app, db)
# manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
