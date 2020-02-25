'''
script to complete matrix data adding zero values (zero padding)
'''

import pandas as pd
import sys

#inputs from command line
idProperties = pd.read_csv(sys.argv[1])
pathInput = sys.argv[2]
pathOutput = sys.argv[3]
valueOfComplete = int(sys.argv[4])
numberSequence = int(sys.argv[5])

for property in idProperties['id_property']:

    nameDoc = pathInput+"property_"+property+".csv"
    matrixData = pd.read_csv(pathInput+"property_"+property+".csv")

    #to replace NaN values for 0...
    matrixData = matrixData.fillna(0)
    lastKey = int(matrixData.keys()[-1])

    #to create array with zero values
    for i in range (valueOfComplete):
        arrayZero = []
        for j in range(numberSequence):
            arrayZero.append(0)
        lastKey+=1
        key = str(lastKey)
        matrixData[key] = arrayZero

    #export data
    nameDoc = pathOutput+"property_"+property+".csv"
    matrixData.to_csv(nameDoc, index=False)    
