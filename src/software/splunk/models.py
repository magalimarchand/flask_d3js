from __future__ import absolute_import
from __future__ import print_function
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import splunklib.client as client

from flask import current_app

#Connection to Inmind's local Splunk installation
class DevSplunk():

	connect=""

	def __init__(self):
		self.connect = client.connect(
		host = current_app.config['SPK_DEV_HOST'],
		port = current_app.config['SPK_DEV_PORT'],
		username = current_app.config['SPK_DEV_USERNAME'],
		password = current_app.config['SPK_DEV_PASSWORD'])

