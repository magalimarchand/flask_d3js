from src import create_app, db
from flask_migrate import MigrateCommand, Manager
from src.authentication.models import User



app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__': 
	manager.run()
	db.create_all()