# Crear un proyecto de Machine Learning

Para crear un proyecto de Machine Learning se recomienda seguir los siguientes pasos:

1. Mirar el panorama general
2. Obtener los datos
3. Descubrir y visualizar los datos para obtener información
4. Preparar los datos para el algoritmo de Machin Learning
5. Seleccionar un modelo y capacitarlo
6. Afinar el modelo
7. Presentarlo
8. Iniciar, monitorear y mantener el sistema

## Trabajar con datos reales

Cuando se quiere aprender Machine Learning es preferible trabajar con datos del mundo real y no con datos artificiales, en el Internet existen muchos conjuntos de datos abiertos.

- Repositorios de datos abiertos populares
  - [Depósito de aprendizaje automático UC Irvine](http://archive.ics.uci.edu/ml/index.php)
  - [Conjuntos de datos de Kaggle](https://www.kaggle.com/datasets)
  - [Conjuntos de datos AWS de Amazon](https://registry.opendata.aws/)
- Meta portales (enumeran repositorios de datos abiertos)

  - [Portales de datos](http://dataportals.org/)
  - [OpenDataMonitor](https://opendatamonitor.eu)
  - [Quandl](https://www.quandl.com/)

- Otras páginas que enumeran muchos repositorios de datos abiertos populares

  - [Lista de Wikipedia de conjuntos de datos de Machine Learning](https://homl.info/9)
  - [Quora.com](https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public)
  - [El subreddit de conjuntos de datos](https://www.reddit.com/r/datasets)

## Mirar la imagen completa

### Enmarcar el problema

Las preguntas para mirar el panorama completo que debe hacer son:

- ¿Cuál es el objetivo comercial del modelo?
- ¿Cómo espera la compañía usar y beneficiarse de este modelo?
- ¿Cómo se ve la solución actual?
- ¿Es supervisado, no supervisado o aprendizaje de refuerzo?
- ¿Es una tarea de clasificación, una tarea de regresión u otra cosa?
- ¿Se debería usar técnicas de aprendizaje por lotes o aprendizaje en línea?

### Seleccionar una medida de rendimiento

Se debe seleccionar una fórmula de medida de rendimiento para ver que tan bueno es el sistema. Entre ellas está:

- Error cuadrático medio (RMSE)
- Error absoluto medio (MAE)

Se pueden ver el archivo [ecuaciones](./Ecuaciones.md).

### Verificar qué se quiere en la salida del modelo

Es importante saber que es lo que se espera en la salida, ya que calcular datos de salida que no son los esperados podría hacernos regresar al principio.

## Obtener los datos

### Descargar los datos

En entornos típicos los datos estarían almacenados en base de datos relacionales o en algún otro almacén de datos común, se deberá ingresar a la base de datos y obtener los datos necesarios.

En algunas ocasiones es necesario realizar funciones especiales para poder obtener los datos y trabajar con ellos.

### Echar un vistazo rápido a la estructura de los datos

Si se trabaja con la librería `pandas` puede utilizar las siguientes funciones para visualizar mejor los datos:

`data.head()` muestra las primeras 5 filas de los datos.

`data.info()` muestra una descripción rápida de los datos.

`data["column"].value_counts()` cuenta cuantos valores hay en cada categoría de la columna.

`data.describe()` obtiene la cantidad de datos, el promedio, la desviación estándar, el valor mínimo, máximo y los 3 percentiles.

`data.hist(bins=50, figsize=(20,15))` `plt.show()` genera un histograma por cada columna.

El vistazo rápido a los datos sirve para detectar cosas en ellos y para entenderlos mejor.

### Crear un conjunto de prueba

Antes de empezar a analizar más los dato hay que hacer un conjunto de pruebas y entrenamiento y dejar el conjunto de pruebas a un lado para después utilizarlo para medir que tan bueno es nuestro sistema.

Se puede generar una función para obtener el conjunto de prueba aleatoriamente:

~~~python
def split_train_test(data, test_ratio):
  shuffled_indices = np.random.permutation(len(data))
  test_set_size = int(len(data) * test_ratio)
  test_indices = shuffled_indices[:test_set_size]
  train_indices = shuffled_indices[test_set_size:]
  return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)
~~~

Pero al volver a obtener los conjuntos dado que son aleatorios serán diferentes, por ello podemos crear una función que obtenga los valores siempre aleatorios pero iguales a la última vez y que podamos agregar más datos.

~~~python
def test_set_check(identifier, test_ratio):
  return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2 ** 32

def split_train_test_by_id(data, test_ratio, id_column):
  ids = data[id_column]
  in_test_set = ids.apply(lambda id_:test_set_check(id_, test_ratio))
  return data.loc[~in_test_set], data.loc[in_test_set]

housing_with_id = housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

print(train_set, test_set)
~~~

`sklearn.model_selection` cuenta con la función `train_test_split()` que divide el conjunto de datos en conjunto de entrenamiento y prueba.

~~~python
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
~~~

Si el conjunto de datos es pequeño al momento de dividirlo puede ocurrir el riesgo de introducir un sesgo de muestreo significativo, para evitarlo se divide el conjunto de datos tomando en cuenta su característica más representativa.