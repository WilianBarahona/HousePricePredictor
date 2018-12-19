from extraer_datos import load_planar_dataset

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
    pass

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
    pass

  def get_datasets(self):
    """Retorna un diccionario con los datasets preprocesados con los datos y 
    dimensiones que se usaron para el entrenamiento
    """"
    X_train, X_test, Y_train, Y_test = load_planar_dataset()

    d = {
    "X_train": X_train,
    "X_test": X_test,
    "Y_train": Y_train,
    "Y_test": Y_test
    }
    
    return dic

