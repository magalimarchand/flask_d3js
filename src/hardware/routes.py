
from flask import render_template, Blueprint, current_app



hardware = Blueprint('hardware', __name__)



### MONITORING
@hardware.route('/hardware/monitoring', methods=['GET','POST'])
def monitoring():
	return render_template('hardware/monitoring.html', title='Hardware monitoring')


### REPORTING
@hardware.route('/hardware/reporting', methods=['GET','POST'])
def reporting():
	return render_template('hardware/reporting.html', title='Hardware reporting')