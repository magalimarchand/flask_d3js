import os

class Config:

	#secret key to protect against modifying cookies & cross-site request forgery attacks
	#command line: $ python >>> import secrets >>> secrets.token_hex(16)
	SECRET_KEY = os.environ.get('SECRET_KEY')

	# ///=relative path to the current file
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

	#email configuration
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	#get my saved credentials in environment variable on my os
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')


	#ELASTICSEARCH configuration
	ES_DEV_HOST = ['http://10.1.5.141:9200','http://10.1.5.142:9200','http://10.1.5.143:9200']
	ES_DEV_INDEX = 'openmind'


	#SPLUNK configuration
	SPK_DEV_HOST = "10.1.5.107"
	SPK_DEV_PORT = 8089
	SPK_DEV_USERNAME = "splninja"  #TO DO: set up in an environment variable
	SPK_DEV_PASSWORD = "d0nTfUckb@sh" #TO DO: set up in an environment variable


	#CENTREON configuration
	CTN_DEV_HOST = "http://10.1.20.49/centreon"
	CTN_DEV_USERNAME = "admin"  #TO DO: set up in an environment variable
	CTN_DEV_PASSWORD = "1234" #TO DO: set up in an environment variable