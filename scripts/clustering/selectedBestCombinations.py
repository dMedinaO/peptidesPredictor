import sys
import pandas as pd

dataElements = pd.read_csv(sys.argv[1])

maxCal = max(dataElements['calinski_harabaz_score'])

dataInfo = ['algorithm','params','groups','calinski_harabaz_score','silhouette_score']

#busco el mayor valor de calinski_harabaz_score
indexArray = []
for i in range(len(dataElements['calinski_harabaz_score'])):
    if maxCal == float(dataElements['calinski_harabaz_score'][i]):
        indexArray.append(i)

print dataElements[dataInfo[0]][indexArray[0]]
print dataElements[dataInfo[1]][indexArray[0]]
print dataElements[dataInfo[2]][indexArray[0]]
print dataElements[dataInfo[3]][indexArray[0]]
print dataElements[dataInfo[4]][indexArray[0]]
