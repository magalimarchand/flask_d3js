from src.analytics.models import Elastic
import json


def getHoursByUser(year, division='Tous'):
	es = Elastic(year)
	query = {
		'size':0,
		'query':{
			'bool':{
				'must':[
					{'range':{'date': es.period}},
					{'match':{'gp division.keyword':division}}
				]     
			}
		},
		'aggs':{
			'users':{'terms':{'field':'user.keyword','size':'200000'},
				'aggs':{'sum_hours':{'sum':{'field':'time (hours)'}}}
			}
		}
	}
	if(division == 'Tous'):
		query['query']['bool']['must'].pop(1)
	query = json.dumps(query)
	results = es.search(query)

	hours_by_user = []
	for k0, v0 in results.items():
		if k0 == 'aggregations':
			for k1, v1 in v0['users'].items():
				if k1 == 'buckets':
					for k2 in v1:
						item = {"user":k2['key'], "hours":round(k2['sum_hours']['value'],2)}
						hours_by_user.append(item)
	return hours_by_user


def getUsers(year):
	es = Elastic(year)
	query = json.dumps({
		'size':0,
			'query':{
				'bool':{
					'must':{
						'range':{'date': es.period}
					}      
				}
			},
			'aggs':{'divisions':{'terms':{'field':'gp division.keyword','size':'200000'},				
				'aggs':{'departments':{'terms':{'field':'gp department.keyword','size':'200000'},
					'aggs':{'users':{'terms':{'field':'user.keyword','size':'200000'},
						'aggs':{'sum_hours':{'sum':{'field':'time (hours)'}
									}
								}
							}
						}
					}
				}
			}
			}
		})
	results = es.search(query)

	all_users = {}
	for division in results['aggregations']['divisions']['buckets']:
		div = {}
		div_total = {} #Total Division array
		depts_list = {} #Departments list array	
		div_hours = 0	#total of hours by division

		for department in division['departments']['buckets']:
			dept = {} # Department array
			dept_total = {} # Total Department array
			users_list = {} # Users list array
			dept_hours = 0  #total of hours by department

			for users in department['users']['buckets']:
				user = {} #User array
				user['total_hours'] = round(users['sum_hours']['value'], 2)
				users_list[users['key']] = user
				#get sum of users hours by department
				dept_hours += users['sum_hours']['value']

			dept_total['total_hours'] = round(dept_hours, 2)
			dept['total'] = dept_total
			dept['users'] = users_list
			depts_list[department['key']] = dept
			#get sum of users hours by division
			div_hours += dept_total['total_hours']

		div_total['total_hours'] = round(div_hours, 2);
		div['total'] = div_total;
		div['departments'] = depts_list;
		all_users[division['key']] = div;
	return all_users
