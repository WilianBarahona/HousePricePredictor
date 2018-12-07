import numpy as np
from houses_container import HousesContainer

# Instancia
contenedorCasas = HousesContainer() 

# Se obtiene la información de las casas y las guarda en contenedor
contenedor = contenedorCasas.get_homes()

# Listas para guardar los datos (atributos)
price = []
location = []
size = []
num_bedrooms = []
num_bathrooms = []
inner_feats = []
outer_feats = []
environ_feats = []

# Listas con todos los diferentes nombres de las caracteristicas
lista_inner_feats = []
lista_outer_feats = []
lista_environ_feats = []

# Vector y matriz que tendran los atributos en forma binaria
vector_atributos = [] # Variable tipo Lista
matriz_atributos = np.zeros(1) # Variable tipo numpy.array

"""
Este método se encarga de generar un vector fila en cada iteración del for
para luego ir agregando cada vector a una matriz.
global: En los metodos python cree que las variables son locales, por
lo tanto se debe de poner de manera explicita que son globales.
"""
def crearMatriz():
  
  global vector_atributos, matriz_atributos
  iniciado = False
  
  for house in contenedor:
    datos = house.get_feats() # Consigue los datos de cada casa en cada iteración
    vector_atributos = [] # Reinicia el vector de atributos en cada iteción
    
    # Al tener las listas de atributos completas, se crean los vectores con 1's y 0's
    for i in lista_inner_feats: # Recorre los inner feats de la lista completa
      if (i in datos['inner_feats']): # Busca si la casa tiene las caracteristicas
        vector_atributos.append("1") # Si la tiene, agrega un 1 en la posición
      else:
        vector_atributos.append("0") # Si no la tiene, agrega un 0 en la posición

    for j in lista_outer_feats: # Recorre los inner feats de la lista completa
      if (j in datos['outer_feats']): # Busca si la casa tiene las caracteristicas
        vector_atributos.append("1")  # Si la tiene, agrega un 1 en la posición
      else:
        vector_atributos.append("0") # Si no la tiene, agrega un 0 en la posición

    for k in lista_environ_feats: # Recorre los inner feats de la lista completa
      if (k in datos['environ_feats']): # Busca si la casa tiene las caracteristicas
        vector_atributos.append("1")  # Si la tiene, agrega un 1 en la posición
      else:
        vector_atributos.append("0") # Si no la tiene, agrega un 0 en la posición
    
    #vector_atributos.append(datos['price']) # Esto es lo que intentamos predecir
    vector_atributos.append(datos['location']) # Agregamos la ubicacion al vector
    vector_atributos.append(datos['size']) # Agregamos el tamaño al vector
    vector_atributos.append(datos['num_bedrooms']) # Agregamos el num de cuartos
    vector_atributos.append(datos['num_bathrooms']) # Agregamos el num de baños
    
    # Convierte la lista a una tupla para que numpy.array pueda aceptar la tupla
    tupla_temp = tuple(vector_atributos) 
    #print("Datos de Tupla:", tupla_temp)
    
    if iniciado == False:
      matriz_atributos = np.array(tupla_temp) # Crear la matriz con los primeros valores
      iniciado = True # Una vez inicializada la matriz, solo queda ir agregando los datoss
    else:
      matriz_atributos = np.vstack([matriz_atributos, tupla_temp])
    
"""
Este método se encarga de crear las 3 listas de caracteristicas, 
luego de analizar todas las casas.
global: En los metodos python cree que las variables son locales, por
lo tanto se debe de poner de manera explicita que son globales.
"""
def crearListas(inner_feats, outer_feats, environ_feats):

  global lista_inner_feats, lista_outer_feats, lista_environ_feats

  # Creacion de las listas con las diferentes caracteristicas
  for i in inner_feats: 
    if (i not in lista_inner_feats):
      lista_inner_feats.append(i)
  
  for j in outer_feats:
    if (j not in lista_outer_feats):
      lista_outer_feats.append(j)

  for k in environ_feats:
    if(k not in lista_environ_feats):
      lista_environ_feats.append(k)

"""
Inicio del programa que obtiene los datos que devulve la funcion get_feats()
"""
for house in contenedor:
  datos = house.get_feats() # Consigue los datos de cada casa en cada iteracion

  # Se desempaqueta el objeto de casas en diferentes listas:
  price.append(datos['price']) # Se agregan los valores a la lista en cada iteración
  location.append(datos['location']) # Se agregan los valores a la lista en cada iteración
  size.append(datos['size']) # Se agregan los valores a la lista en cada iteración
  num_bedrooms.append(datos['num_bedrooms']) # Se agregan los valores a la lista en cada iteración
  num_bathrooms.append(datos['num_bathrooms']) # Se agregan los valores a la lista en cada iteración
  
  inner_feats = datos['inner_feats'] 
  outer_feats = datos['outer_feats']
  environ_feats = datos['environ_feats']

  # Se llama al método que crea las tres listas con una casa a la vez:
  crearListas(inner_feats, outer_feats, environ_feats)
  
  # Prueba de datos:
    #print("Datos:", datos)
    #print("Precio:", price)
    #print("Lugar:", location)
    #print("Tamaño:", size)
    #print("Numero Habitaciones:", num_bedrooms)
    #print("Numero de baños:", num_bathrooms)
    #print("características Interiores:", inner_feats, len(inner_feats))
    #print("características Exteriores:", outer_feats, len(outer_feats))
    #print("características Entorno:", environ_feats, len(environ_feats))

print("----- Lista de Datos Generales de todas las casas -----")
print("Precios:", price) # Vector con los Precios de las n casas
print("Lugares:", location) # Vector con los Lugares de las n casas 
print("Tamaños:", size) # Vector con los Tamaños de las n casas
print("Numero Habitaciones:", num_bedrooms) # Vector con los Habitaciones de las n casas
print("Numero de baños:", num_bathrooms) # Vector con los baños de las n casas

print("----- Lista de Inner feats Totales: -----")
print(lista_inner_feats, ", *Tamaño:", len(lista_inner_feats))
print("----- Lista de Outer feats Totales:  -----")
print(lista_outer_feats, ", *Tamaño:", len(lista_outer_feats))
print("----- Lista de Inv feats Totales: -----")
print(lista_environ_feats, ", *Tamaño:", len(lista_environ_feats))
print("------------------")

# Llama al metodo para crear la matriz que necesitamos
crearMatriz()

print("----- Matriz de Atributos Final: -----")
print(matriz_atributos)



#for i in np.shape(matriz_atributos):
#  print("Fila:", matriz_atributos)
#print("tamaño de la matriz:", np.shape(matriz_atributos))

# Impresion de las Filas:
#print("Fila 01:", matriz_atributos[0])
#print("Fila 02:", matriz_atributos[1])
#print("Fila 03:", matriz_atributos[2])
#print("Fila 04:", matriz_atributos[3])
#print("Fila 05:", matriz_atributos[4])