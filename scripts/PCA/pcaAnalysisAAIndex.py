'''
script que permite implementar PCA para analisis de caracteristicas de la base de datos AAIndex
emplea para ello la libreria scikit-learn.

Se reporta los componentes principales, matriz de componentes, y esquema de componentes en base a aporte de
la varianza.
'''

import pandas as pd
import sys
from sklearn.decomposition import PCA
from sklearn import preprocessing

matrixData = pd.read_csv(sys.argv[1])
pathOutput = sys.argv[2]
requiredStd = int(sys.argv[3])
#variance = float(sys.argv[4])

#estandarizamos el conjunto de datos
min_max_scaler = preprocessing.MinMaxScaler()
matrixData_std = min_max_scaler.fit_transform(matrixData)

pca = PCA(.99999)
matrixData_pca = 0

if requiredStd == 1:#estandar
    #hacemos la ejecucion del PCA
    pca.fit(matrixData_std)
    matrixData_pca = pca.fit_transform(matrixData_std)

else:
    #hacemos la ejecucion del PCA
    pca.fit(matrixData)
    matrixData_pca = pca.fit_transform(matrixData)
header = []

for i in range(pca.n_components_):
    header.append("component_"+str(i+1))

#exportamos el ajuste de los datos transformados, son propiedades ortoganles, la gracia del PCA...
dataComponent = pd.DataFrame(matrixData_pca, columns=header)
dataComponent.to_csv(pathOutput+"data_component.csv", index=False)

#exportamos el aporte de los componentes...
contribution = []

for i in range(len(pca.explained_variance_ratio_)):
    row = ["component_"+str(i+1), pca.explained_variance_ratio_[i]]
    contribution.append(row)

dataContribution = pd.DataFrame(contribution, columns=["component", "variance_ratio"])
dataContribution.to_csv(pathOutput+"data_contribution.csv", index=False)
