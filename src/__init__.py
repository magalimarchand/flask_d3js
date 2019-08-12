from src.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail 


db = SQLAlchemy()
migrate = Migrate()

bcrypt = Bcrypt()

login_manager = LoginManager()
#redirect to login page when route has @login_required decorator
login_manager.login_view = 'authentication.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):

	app = Flask(__name__)

	app.config.from_object(Config)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db.init_app(app)
	migrate.init_app(app, db, render_as_batch=True)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	#at the bottom of the file to avoid circular imports cycles (routes already import app variable)
	from src.main.routes import main
	app.register_blueprint(main)

	from src.errors.handlers import errors
	app.register_blueprint(errors)

	from src.authentication.routes import authentication
	app.register_blueprint(authentication)

	from src.hardware.routes import hardware
	app.register_blueprint(hardware)

	from src.software.elastic.routes import elastic
	app.register_blueprint(elastic)
	
	from src.software.splunk.routes import splunk
	app.register_blueprint(splunk)

	from src.software.centreon.routes import centreon
	app.register_blueprint(centreon)

	from src.mib_interface.visualizations.routes import visualizations
	app.register_blueprint(visualizations)

	from src.examples.routes import examples
	app.register_blueprint(examples)
	
	return app
