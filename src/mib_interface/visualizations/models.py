
class VisualChart():


	#Retrieve a list of JSON arrays and add an id for each visualization
	def getVisualizations(self, datasets):

		visualizations = []
		i=0
		for d in datasets:
			visualizations.append({"id": "chart"+str(i), "dataset": d})
			i += 1

		return visualizations


