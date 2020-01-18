'''
script que permite procesar la data de la matriz obtenida desde el alineamiento,
procesa la data por la posicion y obtiene la frecuencia por cada elemento, genera un archivo resumen con
respecto a las posiciones y un resumen con respecto a la mayor tendencia por cada elemento
'''
import pandas as pd
import sys

matrixAligment = pd.read_csv(sys.argv[1])
numberSequences = len(matrixAligment)
pathOutput = sys.argv[2]
family = sys.argv[3]

listOption = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V', '-']

#obtenemos los ID de las posiciones...
id_pos = list(matrixAligment.keys())
id_seq = id_pos[-1]
id_pos = id_pos[:-1]

dictResponse = {}
matrixData = []

#hacemos la busqueda de las opciones por las posiciones y formamos un diccionarion con respecto a cada opcion en cada posicion
for pos in id_pos:
    dictPosition = {}
    listData = []
    for option in listOption:
        cont_option=0
        for element in matrixAligment[pos]:
             if element == option:
                 cont_option+=1
        cont_option= float(cont_option)*100/float(numberSequences)
        dictPosition.update({option:cont_option})
        listData.append(cont_option)
    dictResponse.update({pos:dictPosition})
    matrixData.append(listData)

#hacemos la traspuesta de la matriz y obtenemos la informacion para dejar en el formato correspondiente
matrixDataT = []
for i in range(len(matrixData[0])):#columns
    rowData = []
    for j in range(len(matrixData)):#rows
        rowData.append(matrixData[j][i])
    matrixDataT.append(rowData)

dataExport = pd.DataFrame(matrixDataT, columns=id_pos)
dataExport['seqID'] = listOption

exportName = pathOutput+"exportAligment_analysis_"+family+".csv"
dataExport.to_csv(pathOutput+"exportAligment_analysis_"+family+".csv", index=False)
