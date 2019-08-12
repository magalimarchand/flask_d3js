
#TRANSFORM DATA FOR CHART VISUALIZATIONS
class DataChart():


	#Transform data for chart dataset with 1 aggregation
	def getDatasetAgg1(self):

		dataset = [
		  {
		    "title": "astmf42.info",
		    "aggregation1": [
		      {"agg1": "Safari","metric1": 702},
		      {"agg1": "Chrome","metric1": 2497},
		      {"agg1": "Firefox","metric1": 497}
		    ]
		  },
		  {
		    "title": "inmindtechnologies.com",
		    "aggregation1": [
		      {"agg1": "Safari","metric1": 1332},
		      {"agg1": "Chrome","metric1": 702},
		      {"agg1": "Internet Explorer","metric1": 92},
		      {"agg1": "Microsoft Edge","metric1": 332},
		      {"agg1": "Firefox","metric1": 2427}
		    ]
		  },
		  {
		    "title": "mindinabox.ca",
		    "aggregation1": [
		      {"agg1": "Safari","metric1": 3614},
		      {"agg1": "Chrome","metric1": 2703},
		      {"agg1": "Firefox","metric1": 602},
		      {"agg1": "Internet Explorer","metric1": 82},
		      {"agg1": "Microsoft Edge","metric1": 332},
		      {"agg1": "Opera","metric1": 1332}
		    ]
		  }
		]

		dataset2 = [
		  {
		    "title": "Marché Jean-Talon",
		    "aggregation1": [
		      {"agg1": "pommes","metric1": 1702},
		      {"agg1": "poires","metric1": 702},
		      {"agg1": "abricots","metric1": 202},
		      {"agg1": "haricots","metric1": 3502},
		      {"agg1": "épinards","metric1": 100},
		      {"agg1": "oranges","metric1": 1497}
		    ]
		  },
		  {
		    "title": "Marché Atwater",
		    "aggregation1": [
		      {"agg1": "pommes","metric1": 2614},
		      {"agg1": "oranges","metric1": 4703},
		      {"agg1": "ananas","metric1": 702},
		      {"agg1": "brocolis","metric1": 332},
		      {"agg1": "asperges","metric1": 133},
		      {"agg1": "salade","metric1": 3702}
		    ]
		  }
		]

		datasets = []
		datasets.append(dataset2)
		datasets.append(dataset)

		return datasets


	#Transform data for chart dataset with 1 aggregation
	def getDatasetVal3(self):

		dataset = [
		  {
		    "title": "openmind",
		    "color": "#008000",
		    "name1":"Canada",
		    "metric1":569,
		    "name2":"World",
		    "metric2":1258
		  },
		  {
		    "title": "astmf42",
		    "color": "#FFD700",
		    "name1":"Canada",
		    "metric1":36,
		    "name2":"World",
		    "metric2":44
		  },
		  {
		    "title": "mindinabox",
		    "color": "#008000",
		    "name1":"Canada",
		    "metric1":12489,
		    "name2":"World",
		    "metric2":18945
		  }
		]


		dataset2 = [
		  {
		    "title": "Montreal_cluster",
		    "color": "#FF0000",
		    "name1":"Ingestion nodes",
		    "metric1":2,
		    "name2":"Total nodes",
		    "metric2":6
		  },
		  {
		    "title": "Laval_cluster",
		    "color": "#008000",
		    "name":"Ingestion nodes",
		    "metric1":3,
		    "name2":"Total nodes",
		    "metric2":5
		  }
		]


		datasets = []
		datasets.append(dataset2)
		datasets.append(dataset)

		return datasets