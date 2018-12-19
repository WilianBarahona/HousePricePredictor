import numpy as np
from houses_container import HousesContainer

"""
Inicio del programa que obtiene los datos que devulve la funcion get_feats()
"""
def crearDatasets():

  # Se crea una instancia
  contenedorCasas = HousesContainer() # Llama al constructor de HousesContainer

  # Se obtiene la información de las casas llamando al metodo get_homes
  # de HousesContainer y las guarda en una variable contenedor
  contenedor = contenedorCasas.get_homes()

  # Listas para guardar los atributos de los datos
  price = []
  location = []
  size = []
  num_bedrooms = []
  num_bathrooms = []
  inner_feats = []
  outer_feats = []
  environ_feats = []

  lista_inner_feats = []
  lista_outer_feats = []
  lista_environ_feats = []
  lista_direccion = []

  # Vector y matriz que tendran los atributos en forma binaria
  vector_etiquetas = np.zeros(1) # Variable tipo numpy.array
  matriz_atributos = np.zeros(1) # Variable tipo numpy.array

  # ** 1. Se inicia en el for, cargando los datos de las casas 
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
    
    # ** 2. Llama al método que crea las tres listas con una casa a la vez **
    lista_inner_feats, lista_outer_feats, lista_environ_feats, lista_direccion = crearListas (inner_feats, outer_feats, environ_feats, location, 
    lista_inner_feats, lista_outer_feats, lista_environ_feats, lista_direccion)
  
  #print("----- Lista de Inner feats: -----")
  #print(lista_inner_feats, ", *Tamaño:", len(lista_inner_feats))
  #print("\n", "----- Lista de Outer feats:  -----")
  #print(lista_outer_feats, ", *Tamaño:", len(lista_outer_feats))
  #print("\n", "----- Lista de Inv feats: -----")
  #print(lista_environ_feats, ", *Tamaño:", len(lista_environ_feats))
  #print("\n", "----- Lista de Direcciones: -----")
  #print(lista_direccion, ", *Tamaño:", len(lista_direccion), "\n") 

  #print("-- Lista de Datos de todas las casas luego de cargarlos todos --")
  #print("Precios:", price, "\n") # Vector con los Precios de las n casas
  #print("Lugares:", location, "\n") # Vector con los Lugares de las n casas 
  #print("Tamaños:", size, "\n") # Vector con los Tamaños de las n casas
  #print("Numero Habitaciones:", num_bedrooms, "\n") # Vector con los Habitaciones de las n casas
  #print("Numero de baños:", num_bathrooms, "\n") # Vector con los baños de las n casas
  #print("características Interiores:", inner_feats, len(inner_feats))
  #print("características Exteriores:", outer_feats, len(outer_feats))
  #print("características Entorno:", environ_feats, len(environ_feats))

  # ** 3. Llama al metodo para crear la matriz que necesitamos **
  matriz_atributos, vector_etiquetas = crearMatrices(lista_inner_feats, lista_outer_feats, lista_environ_feats, lista_direccion)
    
  return matriz_atributos, vector_etiquetas

"""
Este método se encarga de crear las 3 listas de caracteristicas, y la lista
de las direcciones, luego de analizar todas las casas.
"""
def crearListas (inner_feats, outer_feats, environ_feats, location, lista_inner_feats, lista_outer_feats, lista_environ_feats, lista_direccion):

  # Creacion de las listas con las diferentes caracteristicas
  for i in inner_feats: 
    if (i not in lista_inner_feats):
      lista_inner_feats.append(i)
  
  for j in outer_feats:
    if (j not in lista_outer_feats):
      lista_outer_feats.append(j)

  for k in environ_feats:
    if (k not in lista_environ_feats):
      lista_environ_feats.append(k)

  for l in location:
    if (l not in lista_direccion):
      lista_direccion.append(l)

  return lista_inner_feats, lista_outer_feats, lista_environ_feats, lista_direccion

"""
Este método se encarga de generar un vector fila en cada iteración del for
para luego ir agregando cada vector a una matriz X
Tambien crea lo que es el vector Y.
"""
def crearMatrices(lista_inner_feats, lista_outer_feats, lista_environ_feats, lista_direccion):

  contenedorCasas = HousesContainer()
  contenedor = contenedorCasas.get_homes()
  
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

    for j in lista_outer_feats: # Recorre los outer feats de la lista completa
      if (j in datos['outer_feats']): # Busca si la casa tiene las caracteristicas
        vector_atributos.append("1") # Si la tiene, agrega un 1 en la posición
      else:
        vector_atributos.append("0") # Si no la tiene, agrega un 0 en la posición

    for k in lista_environ_feats: # Recorre los environ feats de la lista completa
      if (k in datos['environ_feats']): # Busca si la casa tiene las caracteristicas
        vector_atributos.append("1") # Si la tiene, agrega un 1 en la posición
      else:
        vector_atributos.append("0") # Si no la tiene, agrega un 0 en la posición

    for l in lista_direccion: # Recorre las direcciones de la lista completa
      if (str(l) == str(datos['location'])): # Compara si existe la direccion en los datos
        vector_atributos.append("1") # Si la tiene, agrega un 1 en la posición
      else:
        vector_atributos.append("0") # Si no la tiene, agrega un 0 en la posición
    
    #vector_atributos.append(datos['price']) # Esto es lo que intentamos predecir
    #vector_atributos.append(datos['location']) # La direccion ya se incluyó como 0 y 1
    vector_atributos.append(datos['size']) # Agregamos el tamaño al vector
    vector_atributos.append(datos['num_bedrooms']) # Agregamos el num de cuartos
    vector_atributos.append(datos['num_bathrooms']) # Agregamos el num de baños
    
    if iniciado == False: # Solo va a entrar una vez
      matriz_atributos = np.array(vector_atributos) # Crea la matriz con los primeros valores
      vector_etiquetas = np.array(datos['price']) # Crea el Vector con los primeros valores
      iniciado = True # Una vez inicializada la matriz, solo queda ir agregando los datoss
    else:
      matriz_atributos = np.vstack([matriz_atributos, vector_atributos])
      vector_etiquetas = np.hstack([vector_etiquetas, datos['price']]) #Vector fila de etiquetas Y
  
  #print("----- Matriz Final: -----")
  #print(matriz_atributos) # Es muy grande para imprimirse

  # Impresion de las Filas de toda la matriz (una por una):
  #for i in range(0, len(matriz_transpuesta)):
  #  print("Fila", i,":", matriz_transpuesta[i])

  # Impresiones Manuales de una fila especifica:
  #print("Fila 02:", matriz_transpuesta[1])
  #print("Fila 03:", matriz_transpuesta[2])
  #print("Fila 04:", matriz_transpuesta[3])
  #print("Fila 05:", matriz_transpuesta[4])
  
  #print("----- Vector Fila de Precios: -----")
  #print(vector_etiquetas)

  #print("----- Matriz Transpuesta Final: -----")
  matriz_transpuesta = matriz_atributos.T
  #print(matriz_transpuesta) # Es muy grande para imprimirse

  return matriz_transpuesta, vector_etiquetas

