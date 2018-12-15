import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

print("---------")
newrow = [6,7,8]
A = np.vstack([A, newrow])

print(A)

print("Transpuesta:")
A.T
print(A.T)

print("---------")
matriz = np.zeros(6)
print(matriz)

for i in "Hola":
  vector = [1,2,3,4,5,6]
  matriz = np.array(vector)
  print("Valor")
  print(matriz)

print("Final:", matriz)

print("Prueba para imprimir filas:")
A = np.array([[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

print("A[0] =", A[0]) # First Row
print("A[2] =", A[2]) # Third Row
print("A[-1] =", A[-1]) # Last Row (3rd row in this case)

#print(type(A))
