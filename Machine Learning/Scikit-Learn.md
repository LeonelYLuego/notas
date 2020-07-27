# Scikit-Learn

> Aquí iría la descripción de la librería

## Documentación

`import` importar la librería.

`sklearn.model_selection.train_test_split(housing, test_size=0.2, random_state=42)` función para dividir conjuntos de datos en múltiples conjuntos.

- _test_size_ tamaño del conjunto de prueba.
- _random_state_ semilla de valores aleatorios.

`sklearn.model_selection.StratifiedShuffleSplit()` provee indices de entrenamiento/prueba para dividir el conjunto de entrenamiento/prueba.

- _n_splits_ número de repeticiones de barajado y división.
- _test_size_ tamaño del conjunto de prueba.
- _random_state_ semilla de valores aleatorios.

`sklearn.impute.SimpleImpute` transformador de imputación para completar valores perdidos.

- _strategy_ estrategia de imputación.
  - mean
  - median
  - most_frequent
  - constant
- fit(X) ajusta la imputación en X.
- transform(X) ajusta los datos, luego los transforma.

`sklearn.preprocessing.MinMaxScaler()` transforma los datos en un rango de 0 a 1.

- _feature_range=(0,1)_ rango para transformar los datos.

`sklearn.prerprocesing.StandarScaler()` transforma los datos en una escala estandar.

`sklearn.pepeline.Pipeline` clase para ayudar con secuencias de trasformación.

- _\_\_init\_\_([('name', ClassTransformer()),...])_ constructor que recibe una lista de tuplas con el etiqueta de la transformación y la clase a ejecutar.
- _fit_transform(dataset)_ llama a todas los métodos _fit_transfrom_ de las clases de contructor.

`sklearn.compose.ColumnTransformer` aplica transformaciones a las columnas de un array o `DataFrame` de pandas.

- _\_\_init\_\_([('name', ClassTransformer(), colums),...])_ constructor que recibe una lista de tuplas con el etiqueta de la transformación, la clase a ejecutar y en que columnas aplicar.

