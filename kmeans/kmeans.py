import numpy as np
import random
 
def clusterPoints(data, meansU):
	clusters  = {}
	for x in data:
		bestMeans = min([(i[0], np.linalg.norm(x-meansU[i[0]])) \
			for i in enumerate(meansU)], key=lambda t:t[1])[0]
		try:
			clusters[bestMeans].append(x)
		except KeyError:
			clusters[bestMeans] = [x]
	return clusters
 
def calcCentroids(clusters):
	newMeans = []
	keys = sorted(clusters.keys())
	for k in keys:
		newMeans.append(np.mean(clusters[k], axis = 0))
	return newMeans
 
def checkConverged(meansU, oldMeansU):
	return (set([tuple(i) for i in meansU]) == set([tuple(i) for i in oldMeansU]))
 
def findCentroids(data, K):
    # Initialize to K random centroids
	oldMeansU = random.sample(data, K)
	meansU = random.sample(data, K)
	while not checkConverged(meansU, oldMeansU):
		oldMeansU = meansU
        # Assign all points in X to clusters
		clusters = clusterPoints(data, meansU)
        # Recalc centroids
		meansU = calcCentroids(clusters)
	return (meansU, clusters)

def initData(leng, dataFile):
    data = np.array([(float(dataFile[i][0]), float(dataFile[i][1])) for i in range(leng)])
    return data

# Convert the datas, FLOAT to INT to STRING, and write in a file
def convSaveData(archives, data):

	for x in range(0, 3):
		arrayLen = len(data[x])
		archives.write(("Cluster #"+(str(x+1)))+"\n")
		for y in range(0, arrayLen):
			archives.write(data[x][y][0].astype(int).astype(str))
			archives.write(" ")
			archives.write(data[x][y][1].astype(int).astype(str))
			archives.write("\n")

# First opertations
nameInp = input('Nome do arquivo com dados: ')
nameOut = input('Nome do arquivo gravar dados: ')

archives = open(nameInp, 'r')
dataFile = archives.readlines()
archives.close()

lengArc = len(dataFile)
dataSplit = [i.split() for i in dataFile]

data = initData(lengArc, dataSplit)
means, clusters = findCentroids(data, 3)

archives = open(nameOut, 'w')
convSaveData(archives, clusters)
archives.close()

