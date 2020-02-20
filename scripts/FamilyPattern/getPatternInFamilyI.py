'''
script que permite identificar los distintos motivos conservados y sub clasificar las secuencias existentes en base estos
patrones identificados en los alineamientos multiples
'''

import pandas as pd
import sys
from Bio import SeqIO

#definicion e implementacion de funciones
def searchElementInPositions(star, end, maxGap, sequence):

    count=0
    for i in range(star, end):
        if sequence[i] == "-":
            count+=1

    if count <=maxGap:
        return 0#posee el motivo conservado
    else:
        return 1#no posee el motivo conservado

idSeqs = []

#definicion de variables
dictElement ={"upstream":[], "mthook":[], "PBD":[], "CHR": [], "LBD":[]}#diccionario con la informacion de las secuencias y los motivos conservados

#variables desde linea de comando
alignmentFile = sys.argv[1]

#hacemos la lectura del alineamiento
for record in SeqIO.parse(alignmentFile, "fasta"):

    #buscamos el motivo 1
    response = searchElementInPositions(0, 5, 0, record.seq)
    if response == 0:
        dictElement["upstream"].append(record.id)

    #buscamos el motivo 2
    response = searchElementInPositions(5, 7, 0, record.seq)
    if response == 0:
        dictElement["mthook"].append(record.id)

    #buscamos el motivo 3
    response = searchElementInPositions(7, 15, 0, record.seq)
    if response == 0:
        dictElement["PBD"].append(record.id)

    #buscamos el motivo 4
    response = searchElementInPositions(15, 45, 0, record.seq)
    if response == 0:
        dictElement["CHR"].append(record.id)

    #buscamos el motivo 5
    response = searchElementInPositions(45, 53, 0, record.seq)
    if response == 0:
        dictElement["LBD"].append(record.id)

    idSeqs.append(record.id)

#muestra de elementos por familia sobrelapados...
for element in dictElement:
    print element
    print len(dictElement[element])

matrixDataResponse = []
header = []

#buscamos los elementos unicos en cada familia y las combinaciones de estos...
for idelement in idSeqs:
    rowData = []
    headerData = ["seq"]
    rowData.append(idelement)
    for element in dictElement:
        headerData.append(element)
        if idelement in dictElement[element]:
            rowData.append(1)
        else:
            rowData.append(0)
    matrixDataResponse.append(rowData)
    header = headerData

#formamos un csv con la data y exportamos...
dataFrame = pd.DataFrame(matrixDataResponse, columns=header)
dataFrame.to_csv(sys.argv[2], index=False)
