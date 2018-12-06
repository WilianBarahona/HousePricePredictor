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

def crearVector():
  vecAtributos = []
  for atr in range(len()):
    vecAtributos.append("0")

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

for house in contenedor:
  datos = house.get_feats() # Consigue los datos de cada casa

  # Se desempaqueta el objeto de casas en diferentes listas:
  price = datos['price']
  location = datos['location']
  size = datos['size']
  num_bedrooms = datos['num_bedrooms']
  num_bathrooms = datos['num_bathrooms']
  inner_feats = datos['inner_feats']
  outer_feats = datos['outer_feats']
  environ_feats = datos['environ_feats']

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
print("lista_inner_feats:", lista_inner_feats, len(lista_inner_feats))
print("características Exteriores:", lista_outer_feats, len(lista_outer_feats))
print("características Entorno:", lista_environ_feats, len(lista_environ_feats))

  


