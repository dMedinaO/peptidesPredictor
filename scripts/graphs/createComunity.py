'''
script que permite recibir el archivo de correlacion de las propiedades junto con su codigo correspondiente
y genera una estructura de grafo para poder representar las propiedades y finalmente aplica algoritmos de
busqueda de comunidades y evaluacion de modularidad para obtener las separaciones correspondientes
'''
import sys
import pandas as pd
import networkx as nx
from networkx.algorithms import community
from networkx.algorithms.community import greedy_modularity_communities

dataFrame = pd.read_csv(sys.argv[1])

#creamos la estructura de grafo
graph = nx.Graph()
codeValues = []

#obtenemos el header y los agregamos a los nodos
for element in dataFrame:
    codeValues.append(element)
    graph.add_node(element)

#agrego las aristas
for code in codeValues:
    for i in range(len(dataFrame)):
        if code != codeValues[i]:#solo trabajamos si es diferente de el codigo a evaluar
            value = dataFrame[code][i]
            if value > 0.9:#indica que existe una alta conexion, por lo tanto los elementos son estrechamente relacionados
                graph.add_edge(code, codeValues[i])

c = list(greedy_modularity_communities(graph))

matrix = []
group=1

for element in c:
    for data in element:
        description = searchDescription(data, descriptionValues, codeValues)
        row = [data, "group-"+str(group), description]
        matrix.append(row)
    group+=1

dataFrame = pd.DataFrame(matrix, columns=['property', 'group', 'description'])
dataFrame.to_csv(exportPath+"groupComunity.csv", index=False)
