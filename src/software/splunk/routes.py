from src.software.splunk.utils import getIndexesNameList, createIndexesCSV
from flask import render_template, Blueprint, current_app


splunk = Blueprint('splunk', __name__)



### TEST CONNECTION 
@splunk.route('/splunk/test', methods=['GET','POST'])
def test():

	data = getIndexesNameList()
	return render_template('software/splunk/test.html', title='Splunk test', data=data)


### TEST VISUALIZATION
@splunk.route('/splunk/visualization', methods=['GET','POST'])
def visualization():

	data = getIndexesNameList()

	return render_template('software/splunk/visualization.html', title='Splunk visualization', data=data)


	### TEST VISUALIZATION
@splunk.route('/splunk/visualization2', methods=['GET','POST'])
def visualization2():
	
	data = ""
	#csv = createIndexesCSV()
	return render_template('software/splunk/visualization2.html', title='Splunk visualization')