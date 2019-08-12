from src.software.splunk.models import DevSplunk
import csv

def getIndexesNameList():

	devSplunk = DevSplunk()
	spk = devSplunk.connect

	indexesList=[]
	for index in spk.indexes:
		indexesList.append(index.name)

	return indexesList


def createIndexesCSV():

	devSplunk = DevSplunk()
	spk = devSplunk.connect

	csvData = []
	csvData.append(list(['index','name', 'size']))
	for index in spk.indexes:
			csvData.append(list(['INDEX',index.name, int(index.currentDBSizeMB)]))

	with open('src/static/files/splunk_indexes.csv','w', newline='') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)
