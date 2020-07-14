# Tipos de sistemas de Machine Learning

Los tipos de sistema de Machine Learning se puede clasificar según:

- Estén capacitados con supervisión humana.
- Si pueden o no aprender sobre la marcha.
- Comparando nuevos puntos con puntos antes conocidos o, detectando patrones en los datos de entrenamiento y construyendo un modelo predictivo.

## Aprendizaje supervisado y no supervisado

Los sistemas de Machine Learning se pueden clasificar según la cantidad y tipo de supervisión que reciben durante el entrenamiento.

### Aprendizaje supervisado

En Aprendizaje supervisado, el conjunto de entrenamiento incluye las soluciones deseadas, llamadas etiquetas. Sus tareas típicas son la clasificación y predicción (también llamada regresión).

Para entrenar el sistema se le debe dar muchos ejemplos incluido con sus etiquetas.

#### Algunos de los algoritmos de Aprendizaje supervisado más importantes

- Vecinos k-más cercanos.
- Regresión lineal.
- Regresión logística.
- Máquinas de vectores de soporte(svm).
- Árboles de desición y bosques al azar.
- Redes neuronales.

### Aprendizaje sin supervisión

En el aprendizaje sin supervisión los datos de entrenamiento no está etiquetados, el sistema intenta aprender sin maestro.

#### Algunos de los algoritmos de Aprendizaje no supervisado más importantes

- Agrupamiento
  - k-medias
  - DBSCAN
  - Análisis jerárquico de conglomeraciones (HCA)
- Detección de anomalias y detección de novedades
  - SVM de una clase
  - Kernel PCA
  - Incrustación localmente lineal (LLE)
  - Incrustación de vecinos estocásticos distibuidos en t (t-SNE)
- Asociación de aprendizaje de reglas
  - A priori
  - Eclat

#### Ejemplos

Si se quiere intentar identificar diferentes grupos, por ejemplo clasificar gustos de personas, se puede utilizar un algoritmo de agrupación jerárquica.

Si se quiere reducir los datos sin perder tanta información, por ejemplo la distancia recorrida de un objeto en un tipo determinado, se puede utilizar un algoritmo de reducción de dimensionalidad los fusionará en velocidad.

Si se quiere detectar anomalias, por ejemplo valores atípicos en un conjunto de datos, se puede utilizar un algoritmo de detección de anomalias.

Si se quiere saber que relación tienen unos datos con otros, por ejemplo si las personas personas que compran una película y palomitas también compran salsa, se puede utilizar un algoritmo de aprendizaje de reglas de asociación.

### Aprendizaje semisupervisado

En el aprendizaje semisupervisado los datos están parcialmente etiquetados, esto porque aveces etiquetar todos los datos lleva tiempo.

La mayoría de algoritmos semisupervisados son la combinación de supervisados con no supervisados.

#### Ejemplos

El servicio de Google Fotos reconoce que la persona A está en ciertas fotos (sin supervisión), pero no sabe quién es hasta que le añades una etiqueta para decirle.

### Aprendizaje reforzado

En el aprendizaje reforzado, un agente puede observar el entorno, seleccionar y realizar acciones para obtener una recompensa (negativa o positiva), luego aprende por si mismo cuál es la mejor estrategia.

#### Ejemplos

Un robot que aprende a caminar.

El robot Alpha Go que ganó al mejor jugador de vídeo juegos en el juego Alpha.

## Aprendizaje por Lotes y en Línea

Los sistemas de aprendizaje de Machine Learning también se pueden clasificar: si el sistema puede aprender incrementalmente de un flujo de datos entrantes.

### Aprendizaje por lotes

En el aprendizaje por lotes, el sistema es incapaz de aprender de manera incremental usando todos los datos disponibles ,generalmente fuera de línea, y luego se pone en producción sin tener más aprendizaje. Se llama _aprendizaje fuera de línea_.

Si se quiere que el sistema aprenda nuevos datos, es necesario crear un nuevo sistema con los datos anteriores y los nuevos datos, luego detener el sistema anterior y reemplazarlo con el nuevo. Aunque este proceso se puede automatizar puede llevar varias horas entrenarlo y muchos recursos informáticos por lo que se recomienda actualizarlo cada 24 horas o cada semana.

### Aprendizaje en línea

El aprendizaje en línea es capaz de entrenarse de manera incremental al alimentarlo con instancias de datos secuencialmente, individualmente o en pequeños grupos (minilotes).

Cada paso de este aprendizaje es rápido y económico.

Este sistema es excelente para sistema que reciben datos con flujo continuo y necesitan adaptarse para cambiar de forma rápida o autónoma, además es una buena opción si se tienen recurso informáticos limitados descartando las instancias antiguas que ya no se necesitan e incluso aprendizaje fuera de núcleo.

Es importante tener en cuenta la tasa de aprendizaje, ya que un aprendizaje rápido hará que el sistema olvide los datos rápidamente, mientras que un lento aprendizaje aprenderá más lento pero será menos sensible al ruido de los nuevos datos o datos no representativos.

Un gran desafío con el aprendizaje en línea es que si se ingresan datos incorrectos al sistema el rendimiento de este disminuirá gradualmente, por ello se debe monitorear el sistema de cerca y en caso de ser necesario desactivar el sistema y regresar a una versión anterior.

#### Ejemplos

Sistema para predecir el precio de acciones.

## Aprendizaje basado en Instancias y en Modelos

Los sistemas de aprendizaje de Machine Learning se pueden clasificar por como generalizan.

Dada una serie de ejemplos de capacitación, el sistema debe poder hacer buenas predicciones para generalizar ejemplos que nunca haya visto. El verdadero objetivo es tener un buen desempeño para nuevas instancias.

### Aprendizaje basado en Instancias

Esta es la forma más trivial de aprendizaje porque simplemente aprende de memoria los datos, esto quiere decir que sólo hará predicciones con los datos con el que fue entrenado el sistema.

### Aprendizaje basado en Modelos

Este aprendizaje consiste en crear un modelo con los datos de ejemplo y usar el modelo para predecir los nuevos datos, por ejemplo un modelo de regresión lineal.

###### Ejemplo de código

Digamos que quiere saber qué tan felices son los chipriotas, y los datos de la OCDE no tienen la respuesta, afortunadamente, puede usar su modelo para hacer una buena predicción: buscar el PIB per cápital de Chipre, encuentra $22587 y luego aplica su modelo.

~~~python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

#load the data
oecd_bli = pd.read_csv("https://raw.githubusercontent.com/ClaudiuCreanga/hands-on-machine-learning-scikit-learn-tensorflow-oreilly-geron/master/datasets/lifesat/oecd_bli_2015.csv", thousands=',')
gdp_per_capital = pd.read_csv("https://raw.githubusercontent.com/ClaudiuCreanga/hands-on-machine-learning-scikit-learn-tensorflow-oreilly-geron/master/datasets/lifesat/gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')

#prepare the data
def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

country_stats = prepare_country_stats(oecd_bli, gdp_per_capital)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

#visualize the data
country_stats.plot(kind='scatter', x='GDP per capita', y='Life satisfaction')
plt.show()

#Select a linear model
model = sklearn.linear_model.LinearRegression()

#Train the model
model.fit(X, y)

#Make a prediction for Cyprus
X_new = model.predict([[22587]])
print(X_new)

#Nearest k neighbors
import sklearn.neighbors
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)
model.predict([[22587]])
~~~

