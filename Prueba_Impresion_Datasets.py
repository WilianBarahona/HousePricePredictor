import numpy as np
from houses_container import HousesContainer
from extraccion_comentado import crearDatasets

vector_etiquetas = np.zeros(1) # Variable tipo numpy.array
matriz_atributos = np.zeros(1) # Variable tipo numpy.array

matriz_atributos, vector_etiquetas = crearDatasets()

print("----- Pruebas del laboratorio 3: -----")
### START CODE HERE ### (≈ 3 lines of code)
shape_X = matriz_atributos.shape
shape_Y = vector_etiquetas.shape
m = matriz_atributos.shape[1]  # training set size
### END CODE HERE ###

print ('The shape of X is: ' + str(shape_X))
print ('The shape of Y is: ' + str(shape_Y))
print ('I have m = %d training examples!' % (m))

print("--------------------------------------")
# Impresion de las Filas de toda la matriz:
print("----- Matriz de Atributos Final: -----")
for i in range(0, len(matriz_atributos)):
  print("Fila", i,":", matriz_atributos[i])