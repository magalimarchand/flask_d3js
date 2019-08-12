from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)



# HOME
@main.route('/')
@main.route('/home')
def home(): 
	return render_template('main/home.html', title='Home')

# DOCUMENTATION
@main.route('/documentation')
def documentation(): 
	return render_template('main/documentation.html', title='Documentation')

