#script que permite revisar las propiedades estadisticas de la base de datos AAIndex
import sys
import pandas as pd
import numpy as np
from scipy import stats

database = pd.read_csv(sys.argv[1])

matrixData = []

#por cada elemento obtenemos la informacion estadistica de la data...
for key in database.keys():
    row = []
    row.append(key)
    row.append(np.mean(database[key]))#promedio
    row.append(np.std(database[key]))#desviacion estandar
    row.append(np.var(database[key]))#varianza
    row.append(max(database[key]))#maximo
    row.append(min(database[key]))#minimo

    #aplicamos test de shapiro para evaluar si presenta una distribucion normal o no y con cuanto p-value
    responseShapiro = stats.shapiro(database[key])

    row.append(responseShapiro[1])
    if responseShapiro[1] < 0.05:
        row.append('F')#no distribuye normal
    else:
        row.append('T')#distribuye normal

    matrixData.append(row)

#formamos el dataframe y exportamos la data...
dataframe = pd.DataFrame(matrixData, columns=['key-property', 'mean', 'std', 'variance', 'max-value', 'min-value', 'p-value', 'normal-distribution'])
dataframe.to_csv(sys.argv[2]+"export_statistic_properties.csv", index=False)
