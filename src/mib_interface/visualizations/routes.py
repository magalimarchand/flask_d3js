from flask import render_template, request, Blueprint

#To build url for accessing static css and js files
visualizations = Blueprint('visualizations', __name__, 
								static_url_path='/mib_interface/visualizations/static', 
								static_folder='static')




