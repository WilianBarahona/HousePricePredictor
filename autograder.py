import numpy as np
import math
import matplotlib.pyplot as plt
from os import getcwd, listdir
from os.path import join, isfile

grade = 100
m_train = len(listdir('./casas/train'))
m_test = len(listdir('./casas/test'))

def end_and_print_grade():
  print('=' * 79)
  if grade == 100:
    print('¡Felicidades no se detectó ningún error!')
  print(('Su nota asignada es: NOTA<<{0}>>').format(grade if grade >= 0 else 0))
  exit()

try:
  from house_price_predictor import HousePricePredictor as hpp
except Exception as e:
  print('No se pudo importar la clase HousePricePredictor del módulo house_price_predictor')
  print(('El error recibido fue:\n{0}').format(e))
  grade = 0
  end_and_print_grade()

try:
  hpp = hpp()
except Exception as e:
  print('No se pudo crear una instancia de HousePricePredictor')
  grade = 0
  end_and_print_grade()

try:
  datasets = hpp.get_datasets()
except Exception as e:
  print('No se pudo obtener los datasets -20%')
  print(('El error recibido fue:\n{0}').format(e))
  grade -= 40
else:
  def check_and_save_dataset(dsName, ds, shape):
    global grade
    try:
      if(ds.shape != shape):
        print("{0} no tiene las dimensiones correctas: {1} != {2} -5%".format(
          dsName, str(ds.shape), str(shape)))
        grade -= 5
      print("Salvando {0} en {0}.csv (para revisión del profesor) ...".format(dsName))
      np.savetxt(dsName + ".csv", ds, delimiter=",")
    except Exception as e:
      print('Error al leer {0} -5%'.format(dsName))
      print(('El error recibido fue:\n{0}').format(e))
      grade -= 5
    return
  # number of attrs is read from the dataset
  try:
    n = datasets["X_train"].shape[0]
  except Exception as e:
    print('Error al intentar acceder al dataset X_train -100%')
    print(('El error recibido fue:\n{0}').format(e))
    grade = 0
    end_and_print_grade()

  check_and_save_dataset("X_train", datasets["X_train"], (n,m_train))
  # check_and_save_dataset("X_test", datasets["X_test"], (n,m_test))
  # check_and_save_dataset("Y_train", datasets["Y_train"], (1,m_train))
  # check_and_save_dataset("Y_test", datasets["Y_test"], (1,m_test))

try:
  results = hpp.train_model()
except Exception as e:
  print('Error al entrar el modelo -80%')
  print(('El error recibido fue:\n{0}').format(e))
  grade -= 80
  end_and_print_grade()

try:
  print("Probando parámetros W1, b1, W2 y b2...")
  def predict(W1, b1, W2, b2, X):
    def relu(Z): return np.maximum(0,Z)
    Z1 = W1.dot(X) + b1
    A1 = relu(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = relu(Z2)
    return A2

  W1, b1, W2, b2 = results["W1"], results["b1"], results["W2"], results["b2"]
  Y_train, Y_test = datasets["Y_train"], datasets["Y_test"]
  X_train, X_test = datasets["X_train"], datasets["X_test"]
  Y_prediction_train = predict(W1, b1, W2, b2, X_train)
  Y_prediction_test = predict(W1, b1, W2, b2, X_test)

  print("Raíz cuadrada del error cuadrado medio en train: {}".format(
    math.sqrt(1/(2*m_train) * np.sum(np.power(Y_prediction_train-Y_train,2)))))
  print("Raíz cuadrada del error cuadrado medio en test: {}".format(
    math.sqrt(1/(2*m_test) * np.sum(np.power(Y_prediction_test-Y_test,2)))))
except Exception as e:
  print('Error inesperado al probar parámetros del modelo, es posible que las dimensiones de sus datasets estén incorrectas')
  print(('El error recibido fue:\n{0}').format(e))
  grade -= 80
  end_and_print_grade()

try:
  print("Graficando curva de costos...")
  plt.plot(results['costs'])
  plt.ylabel('cost')
  plt.xlabel('iterations (per hundreds)')
  plt.title("Learning rate =" + str(results["learning_rate"]) + 
            "  Num. Iter =" + str(results["num_iterations"]))
  plt.savefig('./costs_plot.png')
except Exception as e:
  print('Error inesperado al graficar los costos y recuperar el learning_rate y num_iterations')
  print(('El error recibido fue:\n{0}').format(e))
  grade -= 30
  end_and_print_grade()

end_and_print_grade()