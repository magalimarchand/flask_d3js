from src.mib_interface.converters.models import DataChart
from src.mib_interface.visualizations.models import VisualChart
from flask import render_template, Blueprint, current_app

examples = Blueprint('examples', __name__)



### DONUT CHART EXAMPLE
@examples.route('/examples/donutchart', methods=['GET','POST'])
def donutchart():

	#Get datasets
	dataChart = DataChart()
	datasets = dataChart.getDatasetAgg1()

	#Get visualizations
	visualChart = VisualChart()
	donutcharts = visualChart.getVisualizations(datasets)

	return render_template('examples/donutchart.html', title='Donut Chart example',
												donutcharts=donutcharts)



### GAUGE CHART EXAMPLE
@examples.route('/examples/gaugechart', methods=['GET','POST'])
def gaugechart():

	#Get datasets
	dataChart = DataChart()
	datasets = dataChart.getDatasetVal3()

	#Get visualizations
	visualChart = VisualChart()
	gaugecharts = visualChart.getVisualizations(datasets)

	return render_template('examples/gaugechart.html', title='Gauge Chart example',
												gaugecharts=gaugecharts)


	### BARCHART EXAMPLE
@examples.route('/examples/barchart', methods=['GET','POST'])
def barchart():
	
	return render_template('examples/barchart.html', title='Bar Chart example')