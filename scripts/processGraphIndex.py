import pandas as pd
import sys

graphData = pd.read_csv(sys.argv[1])#archivo de grupos con grafo
dbProperties = pd.read_csv(sys.argv[2])#base de datos con propiedades

#obtenemos los elementos unicos de los grupos en las comunidades
id_comunity = list(set(graphData['group']))

for comunity in id_comunity:

    matrixData = []
    matrixData2 = []

    #obtenemos el ID de la propiedad asociado a la comunidad i
    for i in range(len(graphData)):
        if graphData['group'][i] == comunity:
            row = []
            row2 = []
            id_property = graphData['property'][i]
            description = graphData['description'][i]

            #obtenemos los valores para la propiedad...
            valuesProperties = dbProperties[id_property]

            #preparamos el arreglo de valores de propiedades            
            for element in valuesProperties:
                row.append(element)
            row.append(comunity)

            #agregamos a la matriz
            matrixData.append(row)

            #prearamos el arreglo de descripciones
            row2.append(id_property)
            row2.append(description)
            matrixData2.append(row2)

    #formamos el dataframe
    dataframe = pd.DataFrame(matrixData, columns=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V', 'Label'])
    dataframe2 = pd.DataFrame(matrixData2, columns=['idProperty', 'Description'])

    #exportamos la data...
    dataframe.to_csv(sys.argv[3]+str(comunity)+"_properties.csv", index=False)
    dataframe2.to_csv(sys.argv[3]+str(comunity)+"_description.csv", index=False)
