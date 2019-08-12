from src.software.centreon.utils import getHostsNameList
from flask import render_template, Blueprint, current_app


centreon = Blueprint('centreon', __name__)



### CENTREON
@centreon.route('/centreon/test', methods=['GET','POST'])
def test():

	data = ""
	data = getHostsNameList()

	return render_template('software/centreon/test.html', title='Centreon test', 
												data=data)