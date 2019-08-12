from flask_wtf import FlaskForm
from wtforms import SelectField


#select number of data int the CSV to match d3js visualization
class CSVForm(FlaskForm):
	dataCSV = SelectField('Number of data', choices=[(2,'2 datas'),
												(3,'3 datas'),(5,'5 datas')], default=3)



