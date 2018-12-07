from houses_container import HousesContainer

# Instancia
contenedorCasas = HousesContainer() 

# Se obtiene la información de las casas y las guarda en contenedor
contenedor = contenedorCasas.get_homes()

# Listas para guardar los datos
price = []
location = []
size = []
num_bedrooms = []
num_bathrooms = []
inner_feats = []
outer_feats = []
environ_feats = []

# Tamaños para las listas
inner_tam = 0
outer_tam = 0
environ_tam = 0

# Listas con todos los diferentes valores
lista_inner_feats = []
lista_outer_feats = []
lista_environ_feats = []

# Vector que tendra los atributos en forma binaria
vecAtributos = []

def crearVector():
  
  global vecAtributos

  for house in contenedor:
    datos = house.get_feats() # Consigue los datos de cada casa en cada iteracion

    vecAtributos.append("||||||") # Delimitador para indicar cuando termina un vector
    
    for i in lista_inner_feats:
      if (i in datos['inner_feats']):
        vecAtributos.append("1")
      else:
        vecAtributos.append("0")
"""
    for j in lista_outer_feats:
      if (j in datos['outer_feats']):
        vecAtributos.append("1")
      else:
        vecAtributos.append("0")

    for k in lista_environ_feats:
      if (k in datos['environ_feats']):
        vecAtributos.append("1")
      else:
        vecAtributos.append("0")"
"""

"""
Este método se encarga de crear una 3 listas de caracteristicas.
global: En los metodos python cree que las variables son locales, por
lo tanto se debe de poner de manera explicita que son globales.
"""
def crearLista(inner_feats, in_tam, outer_feats, out_tam, environ_feats, env_tam):

  global inner_tam, outer_tam, environ_tam, lista_inner_feats, lista_outer_feats, lista_environ_feats
  
  # Tamaño de los vectores de las caracteristicas
  if (inner_tam < in_tam):
    inner_tam = in_tam
  
  if (outer_tam < out_tam):
    outer_tam = out_tam
  
  if (environ_tam < env_tam): 
    environ_tam = env_tam

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
  price.append(datos['price'])
  location.append(datos['location'])
  size.append(datos['size'])
  num_bedrooms.append(datos['num_bedrooms'])
  num_bathrooms.append(datos['num_bathrooms'])
  
  inner_feats = datos['inner_feats']
  outer_feats = datos['outer_feats']
  environ_feats = datos['environ_feats']

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
  
  # Se crea una lista con una casa a la vez:
  crearLista(inner_feats, len(inner_feats), outer_feats, len(outer_feats), environ_feats, len(environ_feats))

print("------------------")
print("Precios:", price) # Vector con los Precios de las n casas
print("Lugares:", location) # Vector con los Lugares de las n casas 
print("Tamaños:", size) # Vector con los Tamaños de las n casas
print("Numero Habitaciones:", num_bedrooms) # Vector con los Habitaciones de las n casas
print("Numero de baños:", num_bathrooms) # Vector con los baños de las n casas
print("------------------")
print("Lista de Inner feats totales:", lista_inner_feats, ", Tamaño:", len(lista_inner_feats))
#print("Lista de Outer feats totales:", lista_outer_feats, ", Tamaño:", len(lista_outer_feats))
#print("Lista de Inv feats totales:", lista_environ_feats, ", Tamaño:", len(lista_environ_feats))

crearVector()
print("Tamaño del vector: ", len(vecAtributos))
print(vecAtributos)



