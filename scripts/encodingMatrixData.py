'''
Script que permite poder codificar una matriz en base a la estructura que recibe, es decir, procesa un conjunto de
datos que representa secuencias lineales, si tiene gaps, no se consideran y se deja el valor del gap. Recibe tambien
un conjunto de datos que representa los elementos a codificar
Retorna un conjunto de datos por cada componente existente en los elementos empleados a codificar, esto es: si son componentes
de PCA, se generan tantos archivos como componentes tenga el doc, si son propiedades, se genera un archivo codificado por cada
propiedad
'''
