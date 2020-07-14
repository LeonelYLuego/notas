# Principales desafíos del Machine Learning

Las cosas que puede salir mal al intentar crear un sistema con Machine Learning es escoger un algoritmo incorrecto y/o tener datos incorrectos.

## Cantidad insuficiente de datos

El Machine Learning necesita muchos datos para poder funcionar correctamente incluso para problemas muy simples. Sin embargo, debe tenerse en cuenta que los conjuntos de datos de tamaño pequeño y mediano siguen siendo muy comunes, y no siempre es fácil o barato obtener datos de capacitación adicionales.

## Datos de entrenamiento no representativos

Es crucial que los datos de capacitación sean representativos de los nuevos casos a los que se desea generalizar. Al usar un conjunto de entrenamiento no representativo, entrenamos un modelo que es poco probable que haga predicciones precisas, si la muestra es demasiado pequeña tendrá ruido de muestreo.

## Datos de baja calidad

Obviamente si los datos de entrenamiento están llenos de errores, valores atípicos y ruido será más difícil para el sistema detectar los patrones subyacentes, a menudo vale la pena el esfuerzo de pasar tiempo limpiando los datos de entrenamiento, algunos ejemplos de cuando limpiar los datos son:

- Si algunas instancias son claramente atípicas.
- Si a algunas de las instancias les faltan algunas características.

## Características irrelevantes

Es sistema sólo será capaz de aprender si los datos de entrenamiento contienen suficiente características relevantes y no demasiadas irrelevantes.  Una parte crítica del Machine Learning es crear un buen conjunto de características para entrenar. Este proceso implica:

- Selección de características (seleccionando las funciones más útiles para entrenar entre las funciones existentes).
- Extracción de características (combinando características existentes para producir una más útil).
- Crear nuevas funciones mediante la recopilación de nuevos datos.

---

Ahora los problemas al elegir un algoritmo incorrecto.

## Sobreajustar los datos de entrenamiento

En Machine Learning el exceso de generalización, esto se llama sobreajuste: significa que el modelo funciona bien en los datos de entrenamiento, pero no generaliza bien.

Los modelos complejos pueden detectar patrones sutiles en los datos, pero si el conjunto de entrenamiento es ruidoso o si es demasiado pequeño es probable que el modelo detecte patrones en el ruido mismo. Obviamente, estos patrones no se generalizarán en nuevas instancias.

El sobre ajuste ocurre cuando el modelo es demasiado complejo en relación con la cantidad y el ruido de los datos de entrenamiento. Las posibles soluciones son:

- Simplificar el modelo seleccionando uno con menos parámetros, reduciendo el número de atributos en los datos de entrenamiento o restringiendo el modelo (regularización).
- Recopilar más datos.
- Reducir el ruido en los datos de entrenamiento.

## Ajuste insuficiente de los datos de entrenamiento

Un ajuste insuficiente de los datos de entrenamiento ocurre cuando el modelo es demasiado simple para aprender la estructura subyacente de los datos. Las posibles soluciones son:

- Seleccionar un modelo más potente, con más parámetros.
- Alimentar mejores funciones al algoritmo de aprendizaje (ingeniería de características).
- Reducir las restricciones en el modelo. (reduciendo el hiperparámetro de regularización).