#script que permite crear una matriz con la data de los alineamientos de secuencia, exporta la data
#en formato csv para hacer los analisis correspondientes

import pandas as pd
import sys
from Bio import SeqIO

#funcion que permite formar una lista con las letras de la secuencia
def createListOfElement(sequence):

    listData = []
    for i in range(len(sequence)):
        listData.append(sequence[i])
    return listData

alignmentFile = sys.argv[1]
output = sys.argv[2]

sequenceList = []
listID = []

#obtenemos las secuencias y las transformamos en una lista y la almacenamos a la matriz
for record in SeqIO.parse(alignmentFile, "fasta"):

    listID.append(record.id)#el ID
    sequenceList.append(createListOfElement(record.seq))#secuencia

#creamos el header
header = []
for i in range(len(sequenceList[0])):
    element = "pos_"+str(i+1)
    header.append(element)

#creamos un DataFrame
dataExport = pd.DataFrame(sequenceList, columns=header)
dataExport['ID-Seq'] = listID

dataExport.to_csv(output, index=False)#exportamos a csv
