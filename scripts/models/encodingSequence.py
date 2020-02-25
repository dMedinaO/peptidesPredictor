'''
script to encoding sequence in family, for each property to use, to create a file with encoding information and
export sequence data in format split information
'''

#imports modules secction
import pandas as pd
import sys
from Bio import SeqIO

#function to get value of property for a residue
def getValueOfResidue(residue, listProperty, listResidue):

    index=0

    for i in range(len(listResidue)):
        if listResidue[i] == residue:
            index=i
            break
    return listProperty[index]

#inputs from command line
familyInput = sys.argv[1]
idProperties = pd.read_csv(sys.argv[2])
matrixAAIndex = pd.read_csv(sys.argv[3])
pathOutput = sys.argv[4]

#process sequence data and save in array structure
sequenceData = []
idSequence = []

for record in SeqIO.parse(familyInput, "fasta"):
    sequenceData.append(record.seq)
    idSequence.append(record.id)

#for each ID in list of properties, encoding sequence
for keyData in idProperties['id_property']:

    lenArray= []
    matrixData_encoded = []
    for sequence in sequenceData:
        #work with elements in sequence
        rowData = []
        for residue in sequence:
            valueData = getValueOfResidue(residue, matrixAAIndex[keyData],matrixAAIndex['residue'])
            rowData.append(valueData)

        matrixData_encoded.append(rowData)
        lenArray.append(len(rowData))

    maxData = max(lenArray)

    #to create header for dataFrame
    header = []
    for i in range(maxData):
        header.append(str(i+1))

    #to create Data Frame
    dataFrameExport = pd.DataFrame(matrixData_encoded, columns=header)

    #to export data Frame
    nameDoc = pathOutput+"property_"+keyData+".csv"
    dataFrameExport.to_csv(nameDoc, index=False)

#finally, export a data frame with index id of sequence
dataFrameIndex= pd.DataFrame(idSequence, columns=['idSequence'])
dataFrameIndex.to_csv(pathOutput+"index_sequence.csv", index=False)
