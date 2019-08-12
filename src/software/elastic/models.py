from flask import current_app
from elasticsearch import Elasticsearch
import requests

#Connection to Magali's local Centreon installation
class DevElastic():

	es = ""
	index = ""
	period = []

	def __init__(self, year=None):
		self.es = Elasticsearch(current_app.config['ES_DEV_HOST'])
		self.index = current_app.config['ES_DEV_INDEX']
		if(year!=None):
			date = {}
			date['gte'] = str(year-1)+'-09-01T00:00:00.000Z'
			date['lte'] = str(year)+'-09-01T00:00:00.000Z'
			self.period = date


	def search(self, body):
		results = self.es.search(index=self.index, body=body, request_timeout=30)
		return results


class DevCluster():

	es = ""

	def __init__(self):
		self.es = Elasticsearch(current_app.config['ES_DEV_HOST'])

	def health(self):
		results = self.es.cluster.health(request_timeout=30)
		return results