from flask_wtf import FlaskForm
from wtforms import SelectField


#DATE, DIVISION, DEPARTMENT DROPDOWN
class Form(FlaskForm):
	period = SelectField('Période', choices=[(2017,'du 2017-09-01 au 2018-08-31'),
																			(2018,'du 2018-09-01 au 2019-08-31')], default=2017)
	division = SelectField('Division', choices=[], default='Tous', id='d')


