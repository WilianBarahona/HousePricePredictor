import numpy as np
from houses_container import HousesContainer
from extraccion_comentado import crearDataSets

# X_train = np.zeros(1,dtype=int) # Variable tipo numpy.array
# Y_train = np.zeros(1,dtype=int) # Variable tipo numpy.array
# X_test = np.zeros(1,dtype=int) # Variable tipo numpy.array
# Y_test = np.zeros(1,dtype=int) # Variable tipo numpy.array

X_train, Y_train = crearDataSets('casas/train/')
X_test, Y_test = crearDataSets('casas/test/')

print("----- Train: -----")
shape_X = X_train.shape
shape_Y = Y_train.shape
m = X_train.shape[1]  # Tamaño del conjunto entrenamiento

print ('The shape of X is: ' + str(shape_X))
print ('The shape of Y is: ' + str(shape_Y))
print ('I have m = %d training examples!' % (m))

print("----- Test: -----")
shape_X = X_test.shape
shape_Y = Y_test.shape
m = X_test.shape[1]  # Tamaño del conjunto entrenamiento

print ('The shape of X is: ' + str(shape_X))
print ('The shape of Y is: ' + str(shape_Y))
print ('I have m = %d training examples!' % (m))

print("--------------------------------------")
# Impresion de las Filas de toda la matriz:
#print("----- Matriz de Atributos X_train Final: -----")
#for i in range(0, len(X_train)):
#  print("Fila", i,":", X_train[i])

print("--------------------------------------")
# Impresion de las Filas de toda la matriz:
print("----- Matriz de Atributos X_test Final: -----")
for i in range(0, len(X_test)):
  print("Fila", i,":", X_test[i])

# Impresion incompleta de las matrices
#print(X_train)
#print(Y_train)
#print(X_test)
#print(Y_test)