from src.software.elastic.utils import getHoursByUser, getUsers, getClusterHealth
from src.software.elastic.forms import Form
from flask import render_template, Blueprint, current_app
from datetime import datetime



elastic = Blueprint('elastic', __name__)


### MONITORING
@elastic.route('/elasticsearch/monitoring', methods=['GET','POST'])
def monitoring():

	data = getClusterHealth()
	return render_template('software/elastic/monitoring.html', title='Elasticsearch monitoring',
													data=data)



### CDAE
@elastic.route('/elasticsearch/d3js', methods=['GET','POST'])
def d3js(): 

	form = Form()

	#period dropdown
	year = int(form.period.data)

	#division dropdown
	divisions = []
	divisions.append(["Tous","Tous"])
	results = getUsers(year)
	for divs, depts in results.items():
		data = [divs,divs]
		divisions.append(data)
	form.division.choices = divisions

	#d3js barchart data
	hours_by_user = getHoursByUser(year, form.division.data)

	return render_template('software/elastic/d3js.html', title='d3js visualizations', 
													form=form, data=hours_by_user)



### KIBANA DASHBOARDS
@elastic.route('/elasticsearch/kibana', methods=['GET','POST'])
def kibana():
	return render_template('software/elastic/kibana.html', title='Kibana dashboards')

