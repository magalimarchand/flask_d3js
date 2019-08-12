VIRTUAL ENVIRONMENT

To create a virtual environment 
	$ virtualenv env
To activate and start the virtual environment
	$ env\Scripts\activate

To find my site packages
	$ python
	>>> import site
	>>> site.getsitepackages()

#####################################################

START THE PROJECT

You have to set the FLASK_APP (replace 'set' by 'export' for Linux)
	(venv)$ set FLASK_APP=run.py

To activate debug mode
	(venv)$ set FLASK_DEBUG=1

Start the application
	(venv)$ flask run

#####################################################

DB MIGRATION

To initialize the db migration module (flask-migrate)
	(venv)$ flask db init
	(venv)$ flask db migrate

To apply the migration to the database
	(venv)$ flask db upgrade

#####################################################

EXTERNAL PACKAGES

To add all required packages for the application from a new installation:
	(venv)$ pip install -r requirements.txt

To individually add all required external packages for the application:
	(venv)$ pip install flask-wtf
	(venv)$ pip install flask-sqlalchemy
	(venv)$ pip install flask-bcrypt
	(venv)$ pip install flask-login
	(venv)$ pip install Pillow  #to resize images (from PIL import Image)
	(venv)$ pip install flask-mail
	(venv)$ pip install elasticsearch
	(venv)$ pip install requests
	(venv)$ pip install -U googlemaps
	(venv)$ pip install pandas
	(venv)$ pip install numpy
	(venv)$ pip install Flask-Migrate

To write/update the requirements.txt file when a package has been added individually:
	(venv)$ pip freeze > requirements.txt

#####################################################

MODULE

Each entity (authentication, main, blog, ...) must have a __init__.py file in its folder, even if it's empty, to specify the folder is a module.

#####################################################

BLUEPRINT

Each blueprint must be initialized into its routes.py file:
	from flask import Blueprint
	main = Blueprint('main', __name__)

In the root __init__.py file, each blueprint must be imported and registered:
	from src.main.routes import main
	app.register_blueprint(main)

#####################################################

ENVIRONMENT VARIABLES

In the root config.py file, several variables have their values imported from the environment variables of the OS where the app is installed:
	# in my os: SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

To configure PYTHONPATH system environment variable, add python37 location and its Lib location
$ where python

#####################################################

SPLUNK SDK

You have to manually install splunk-sdk if you want to use the examples. pip installation does not include examples.

#####################################################

TUTORIAL

YouTube tutorial to create this blog app:
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

Other material
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://flask-migrate.readthedocs.io/en/latest/
https://www.tutorialspoint.com/flask/index.htm
https://pandas.pydata.org/
http://book.pythontips.com/en/latest/
