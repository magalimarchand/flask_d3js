from src.software.centreon.models import DevCentreon


def getHostsNameList():

	devCentreon = DevCentreon()
	ctn = devCentreon.connect

	hostsList=[]
	for host in ctn.hosts.list():
		hostsList.append(host)
	return hostsList

