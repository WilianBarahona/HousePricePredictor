import numpy as np
import matplotlib.pyplot as plt
from os import getcwd
from os.path import join

grade = 100
m_train = 122
m_test = 43

def end_and_print_grade():
  print('=' * 79)
  if grade == 100:
    print('¡Felicidades no se detectó ningún error!')
  print(('Su nota asignada es: NOTA<<{0}>>').format(grade if grade >= 0 else 0))
  exit()

try:
  from house_price_predictor import HousePricePredictor as hpp
except Exception as e:
  print('No se pudo importar la clase HousePricePredictor del módulo sentiment')
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
  check_and_save_dataset("X_test", datasets["X_test"], (n,m_test))
  check_and_save_dataset("Y_train", datasets["Y_train"], (1,m_train))
  check_and_save_dataset("Y_test", datasets["Y_test"], (1,m_test))

try:
  results = hpp.train_model()
except Exception as e:
  print('Error al entrar el modelo -80%')
  print(('El error recibido fue:\n{0}').format(e))
  grade -= 80
  end_and_print_grade()

try:
  print("Probando parámetros W y b...")
  def predict(w, b, X):
    def sigmoid(z): return (1 / (1 + np.exp(-z)))
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(w.T.dot(X) + b)
    return (A > 0.5).astype(int)

  w, b = results["w"], results["b"]
  Y_train, Y_test = datasets["Y_train"], datasets["Y_test"]
  X_train, X_test = datasets["X_train"], datasets["X_test"]
  Y_prediction_train, Y_prediction_test = predict(w,b,X_train), predict(w,b,X_test)
  print("Precisión en train: {} %".format(
    100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
  print("Precisión en test: {} %".format(
    100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))
except Exception as e:
  print('Error inesperado al probar parámetros w y b, es posible que las dimensiones de sus datasets estén incorrectas')
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