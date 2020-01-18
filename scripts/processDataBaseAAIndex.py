'''
script que permite procesar la base de datos AAIndex y dejar una matriz de tamano 20 x 560~
esta matriz permitira trabajar con los PCA lineales, tecnicas de reduccion no lineales...
'''
import pandas as pd
import sys

#lectura de los conjuntos de datos
matrixData = pd.read_csv(sys.argv[1])#db_aaindex.csv
matrixFull = pd.read_csv(sys.argv[2])#db_codes_properties.csv
pathOutput = sys.argv[3]

#obtenemos la data de los residuos
keysData = list(matrixData.keys())
keysData = keysData[2:]

matrixFull['residue'] =keysData

matrixFull.to_csv(pathOutput+"db_codes_properties_with_res.csv", index=False)
