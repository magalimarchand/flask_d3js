from centreonapi.centreon import Webservice, Centreon
from flask import current_app

#Connection to Magali's local Centreon installation
class DevCentreon():

	connect=""

	def __init__(self):
		self.connect = Centreon(
		current_app.config['CTN_DEV_HOST'],
		current_app.config['CTN_DEV_USERNAME'],
		current_app.config['CTN_DEV_PASSWORD'])