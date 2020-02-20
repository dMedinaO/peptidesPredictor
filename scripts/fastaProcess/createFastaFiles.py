#script para crear archivos fasta con los peptidos a partir de archivos csv con la informacion, recibe la Familia

import pandas as pd
import sys

#funcion que permite crear archivo fasta con la informacion de los peptidos segun familia
def createFastaFile(listSequence, listNames, nameFile, family):

    fileWrite = open(nameFile, 'w')

    for i in range(len(listSequence)):
        line = ">%s %s" % (family, listNames[i])
        fileWrite.write(line+"\n")
        fileWrite.write(listSequence[i]+"\n")

    fileWrite.close()

docInput = pd.read_csv(sys.argv[1])
pathOutput = sys.argv[2]
familyList = list(set(docInput['Family']))

for element in familyList:
    matrixSequence = []
    matrixNames = []

    for i in range(len(docInput)):
        if docInput['Family'][i] == element:
            matrixSequence.append(docInput['SECUENCIA'][i])
            matrixNames.append(docInput['NOMBRE'][i])

    nameDoc = "%s%s_family.fasta" % (pathOutput, element)
    print "export doc: ", nameDoc
    createFastaFile(matrixSequence, matrixNames, nameDoc, element)
