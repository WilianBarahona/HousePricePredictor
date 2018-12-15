from house import House
import os 

class HousesContainer:
  """ 
  Representa un contenedor de casas, específicamente de objetos de tipo House.
  """

  ## ==== Constructor ==== ##
  def __init__(self):
    """
    En el constructor se leen todos los archivos con extensión html que están 
    en el directorio '/casas'.

    El contenido de cada archivo html se lee en una cadena que se usa para 
    crear un objeto de tipo House. 
    """
    
    ## ==== Leer archivos html ==== ##
    #archivo = open("casas/10053.html", "r", encoding='utf-8') # encoding = 'utf-8' para windows
    
    list_file_html = [] # Declaracion de la Lista
    files = os.listdir('./casas/test')
    
    for file in files:
      if '.html' in file:
        list_file_html.append(file)

    # print("Lista de archivos html:", list_file_html)
    # ['10053.html', '10264.html', '10564.html', '10567.html', '8696.html']

    self.list_houses = [] # Lista para accederla desde otra clase
    
    for file_html in list_file_html:
      archivo = open("casas/test/" + file_html, "r", encoding = 'utf-8')
      self.list_houses.append(House(archivo.read(), file_html))
      #self.casa = House(archivo.read(), file_html)
    
    """
    get_homes()
    Retorna un lista que contiene todo los objetos de tipo House creados en el constructor.
    """

  ## ==== Metodo get_homes ====  ##
  def get_homes(self):
    list_get_homes = []
    for l in self.list_houses:
      list_get_homes.append(l.get_feats())
    # return self.list_houses[4].get_feats()
    return self.list_houses

contenedor = HousesContainer()
c = contenedor.get_homes()
# print(c)
# c = contenedor.get_homes().get_feats()
# dic = contenedor.casa.get_feats()
# print(dic)