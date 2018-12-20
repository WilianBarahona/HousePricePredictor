from extraccion_comentado import crearDataSets
import numpy as np

class HousePricePredictor:

  def __init__(self):
    """El método init leerá todos los archivos con extensión ".html" de los directorios casas/train y casas/test y los usará para crear las matrices de X_train, X_test, Y_train y Y_test.

    Cada archivo con formato "html" corresponderá a una instancia de entrenamiento o prueba. Deberá leer los atributos de cada casa tomando como base el código del proyecto anterior:

    {
      "price": "6370597",
      "size": "267",
      "num_bedrooms": "4",
      "num_bathrooms": "3.5",
      "location": "Colonia Alameda, Tegucigalpa, Francisco Morazán",
      "inner_feats": {"cisterna", "comedor", "sistema de alarma"},
      "outer_feats": {"garaje: si", "cuarto de servidumbre", "estudio", "sala"},
      "environ_feats: {"area social"}
    }

    Sin embargo, antes de poder entrenar un modelo deberá convertir estos atributos a valores numéricos, los atributos size, num_bedrooms y num_bathrooms ya tienen valores numéricos, el atributo price también, pero este no se considerará como atributo, sino como la etiqueta de la instancia.

    Para el resto de atributos, es decir: location, inner, outer y environ feats deberá utilizar la técnica conocida como One Hot Encoding (explicada en clase) para generar vectores binarios para cada atributo y unirlos al final en el vector de atributos definitivo. 

    """
    print("Generando el Dataset de Entrenamiento...")
    self._X_train, self._Y_train = crearDataSets('casas/train/') # Entrenamiento
    print("Generando el Dataset de Prueba...")
    self._X_test, self._Y_test = crearDataSets('casas/test/') # Prueba
    print("Datasets Generados.")
   
  def train_model(self):
    """Retorna un un diccionario con los siguientes datos:
    
    d = {"costs": costs,
    "w1" : w1, 
    "b1" : b1,
    "w2" : w2,
    "b2" : b2
    "learning_rate" : learning_rate,
    "num_iterations": num_iterations}
    
    costs, es una lista con los costos obtenidos durante el entrenamiento cada 100 interaciones. learning_rate y num_iterations deben ser definidos por el programador mediante un proceso de prueba y error con el fin de obtener la mejor precisión en los datos de prueba.
    """
    ### --Inicio red neuronal superfial--- ###
    X = self._X_train
    Y = self._Y_train

    n_x, n_h, n_y = layer_sizes(X, Y) # Llama a la función 1.
    #print("The size of the input layer is: n_x = " + str(n_x))
    #print("The size of the hidden layer is: n_h = " + str(n_h))
    #print("The size of the output layer is: n_y = " + str(n_y))
    learning_rate = 0.001 # Hay que ver que tan alto o bajo será el learning rate
    num_iterations = 8000 # Habra que ver cuantas iteraciones es un numero aceptable
    parameters = initialize_parameters(n_x, n_h, n_y) # Llama a la función 2.
    dicOut = nn_model(X, Y, n_h, num_iterations , True) #True = imprimir costo , False = no imprimir el costo

    return dicOut

  def get_datasets(self):
    """Retorna un diccionario con los datasets preprocesados con los datos y 
    dimensiones que se usaron para el entrenamiento
    """
    d = {
      "X_train": self._X_train,
      "Y_train": self._Y_train,
      "X_test": self._X_test,
      "Y_test": self._Y_test
    }
    
    return d

