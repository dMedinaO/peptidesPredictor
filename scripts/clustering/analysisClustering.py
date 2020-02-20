import pandas as pd
import sys

responseClustering = pd.read_csv(sys.argv[1])
properties_desc = sys.argv[2]
idElement = pd.read_csv(sys.argv[3])

idElement = idElement['Code']

#obtenemos la informacion de las propiedades
descriptionArray = []

fileOpen = open(properties_desc, 'r')
line = fileOpen.readline()

while line:
    data = line.replace("\n", "")
    descriptionArray.append(data)
    line = fileOpen.readline()

#obtenemos el numero de grupos y separamos por propiedades...
labels = list(set(responseClustering['Labels']))

for label in labels:
    matrixData = []
    matrixData2 = []
    for i in range(len(responseClustering)):
        if responseClustering['Labels'][i] == label:
            row = []
            for key in responseClustering.keys():
                row.append(responseClustering[key][i])
            matrixData.append(row)
            row2 = []
            row2.append(idElement[i])
            row2.append(descriptionArray[i])
            matrixData2.append(row2)

    #formamos el dataframe
    dataframe = pd.DataFrame(matrixData, columns=responseClustering.keys())
    dataframe2 = pd.DataFrame(matrixData2, columns=['idProperty', 'Description'])

    #exportamos la data...
    dataframe.to_csv(sys.argv[4]+str(label)+"_properties.csv", index=False)
    dataframe2.to_csv(sys.argv[4]+str(label)+"_description.csv", index=False) 
