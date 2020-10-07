# Scikit-Learn

## `sklearn.model_selection`

El módulo `sklearn.model_selection` contiene clases y funciones de divisores, optimizadores de hiperparámetros y validación de modelos.

### Clases de divisores

~~~python
from sklearn.model_selection import StratifiedShuffleSplit #Proporciona índices de entrenamiento/prueba para dividir datos en conjunto de entrenamiento/prueba.
from sklearn.model_selection import StratifiedKFold #Proporciona índices de entrenamiento/prueba para dividir datos en conjunto de entrenamiento/prueba.
~~~

### Funciones de divisores

~~~python
from sklearn.model_selection import train_test_split #Divide arreglos o matrices en conjuntos de entrenamiento y prueba aleatorios.
~~~

### Optimizadores de hiperparámetros

~~~python
from sklearn.model_selection import GridSearchCV #Búsqueda exhaustiva de valores de parámetros especificados para un estimador.
from sklearn.model_selection import RandomSearchCV #Búsqueda aleatoria de hiperparámetros.
~~~

### Validación de modelos

~~~python
from sklearn.model_selection import cross_val_score #Evalua una puntuación mediante validación cruzada.
from sklearn.model_selection import cross_val_predict #Genera estimaciones con validación cruzada para cada punto de datos de entrada.
~~~

## `sklearn.preprocessing`

El paquete `sklearn.preprocessing` proporciona varias funciones de utilidad comunes y clases de transformadores para cambiar los vectores de características sin procesar en una representación que sea más adecuada para los estimadores posteriores.

~~~python
from sklearn.preprocessing import OrdinalEncoder #Codifica características categóricas como una matriz de números enteros.
from sklearn.preprocessing import OneHotEncoder #Codifique características categóricas como una matriz numérica única.
from sklearn.preprocessing import StandardScaler #Estandariza las características eliminando la media y escalando a la varianza de la unidad.
~~~

## `sklearn.base`

Usado para VotingClassifier

~~~python
from sklearn.base import BaseEstimator #Clase base para todos los estimadores en scikit-learn.
from sklearn.base import TransformerMixin #Clase Mixin para todos los transformadores en scikit-learn.
from sklearn.base import clone #Construye un estimador nuevo con los mismos parámetros.
~~~

## `sklearn.linear_model `

El módulo `sklearn.linear_model` implementa una variedad de modelos lineales.

~~~python
from sklearn.linear_model import LinearRegression #Regresión lineal por mínimos cuadrados ordinarios.
from sklearn.linear_model import SGDClassifier #Clasificadores lineales (SVM, regresión logística, etc.) con entrenamiento SGD.
~~~

## `sklearn.impute`

Transformadores para imputación de valor faltante.

~~~python
from sklearn.impute import SimpleImputer #Transformador de imputación para completar valores perdidos.
~~~

## `sklearn.pipeline`

El módulo `sklearn.pipeline` implementa utilidades para construir un estimador compuesto, como una cadena de transformaciones y estimadores.

~~~python
from sklearn.pipeline import Pipeline #Tubería de transformaciones con un estimador final.
~~~

## `sklearn.compose`

Metaestimadores para la construcción de modelos compuestos con transformadores.

~~~python
from sklearn.compose import ColumnTransformer #Aplica transformadores a columnas de una matriz o pandas DataFrame.
~~~

## `sklearn.metrics`

Métricas.

### Métricas de clasificación

~~~python
from sklearn.metrics import confusion_matrix #Calcula la matriz de confusión para evaluar la precisión de una clasificación.
from sklearn.metrics import precision_score #Calcula la precisión.
from sklearn.metrics import recall_score #Calcular la recuperación.
from sklearn.metrics import f1_score #Calcula la puntuación F1, también conocida como puntuación F-equilibrada o F-medida
from sklearn.metrics import precision_recall_curve #Calcula pares de recuperación de precisión para diferentes umbrales de probabilidad.
from sklearn.metrics import roc_curve #Calcula característica operativa del receptor de cálculo (ROC).
from sklearn.metrics import roc_auc_score #Calcula el área bajo la curva de características operativas del receptor (ROC AUC) a partir de las puntuaciones de predicción.
~~~

### Métricas de regresión

~~~python
from sklearn.metrics import mean_squared_error #Pérdida de regresión del error cuadrático medio
~~~

## `sklearn.tree`

El módulo `sklearn.tree` incluye modelos basados en árboles de decisión para clasificación y regresión.

~~~python
from sklearn.tree import DecisionTreeRegressor #Un regresor de árbol de decisión.
~~~

## `sklearn.ensemble`

El módulo `sklearn.ensemble` incluye métodos basados en conjuntos para clasificación, regresión y detección de anomalías.

~~~python
from sklearn.ensemble import RandomForestRegressor #Bosque aleatorio de regresión.
from sklearn.ensemble import RandomForestClassifier #Bosque aleatorio de clasificación.
~~~

##  `sklearn.datasets`

El módulo `sklearn.datasets` incluye utilidades para cargar conjuntos de datos, incluidos métodos para cargar y recuperar conjuntos de datos de referencia populares. También cuenta con algunos generadores de datos artificiales.

~~~python
from sklearn.datasets import fetch_openml #Obtener el conjunto de datos de openml por nombre o id del conjunto de datos.
~~~

## `sklearn.svm`

El módulo `sklearn.svm` incluye algoritmos de Support Vector Machine.

~~~python
from sklearn.svm import SVC #Clasificación de vectores de soporte C.
~~~

## `sklearn.multiclass`

Estrategias de clasificación multiclase y multilabel.

~~~python
from sklearn.multiclass import OneVsRestClassifier #Estrategia multiclase / multilabel de uno contra el resto (OvR)
~~~

## `sklearn.neighbors`

El módulo `sklearn.neighbors` implementa el algoritmo de k vecinos más cercanos.

~~~python
from sklearn.neighbors import KNeighborsClassifier #Clasificador que implementa el voto de los k vecinos más cercanos.
~~~



