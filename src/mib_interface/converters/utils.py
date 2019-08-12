import csv

#create a csv with 3 data by row to match some d3js visualizations (multiple_donuts)
def downloadCSV():

	devSplunk = DevSplunk()
	spk = devSplunk.connect

	csvData = []
	csvData.append(list(['index','name', 'size']))
	for index in spk.indexes:
			csvData.append(list(['INDEX',index.name, int(index.currentDBSizeMB)]))

	with open('src/static/files/splunk_indexes.csv','w', newline='') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)
