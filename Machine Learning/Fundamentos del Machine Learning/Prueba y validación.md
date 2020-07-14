# Prueba y validación

La única manera de saber qué tan bien se generalizará un modelo a casos nuevos es probarlo en casos nuevos. Ya sea poniéndolo en producción y monitorear que tan bien funciona y separando los datos en dos conjuntos: el conjunto de entrenamiento y conjunto de prueba, al evaluar el modelo con el conjunto de prueba obtiene una estimación al error de generalización.

Si el error de entrenamiento es bajo pero el error de generalización es alto, significa que el modelo está sobreajustando los datos del entrenamiento.

Es común usar el 80% de los datos para entrenar y el 20% para pruebas.

## Ajuste de hiperparámetros y selección de modelo

Supongamos que existen dos modelos posibles para solucionar un problema, ¿qué modelo elegir?, una opción es entrenar a ambos y compara qué tan bien generalizan usando el conjunto de prueba.

Ahora suponga que un modelo generaliza mejor, pero se desea aplicar alguna regularización para evitar el sobreajuste, la pregunta es ¿cómo elegir el valor del hiperparámetro de regularización?. Una opción es entrenar 100 modelos diferentes con 100 valores de hiperparámetro diferente y se encuentra un modelo que tiene un error bajo, pero se lanza a producción y produce un un error más alto.

Una solución común a este problema se llama validación de reserva, simplemente se tiene una parte del conjunto de capacitación para evaluar varios modelos candidatos y seleccionar el mejor. El nuevo conjunto extendido se llama conjunto de validación. Más específicamente, se entrena múltiples modelos con varios hiperparámetros en el conjunto de entrenamiento reducido y se selecciona el modelo que funciona mejor en el conjunto de validación. Después este proceso de validación, se entrena el mejor modelo en el conjunto completo de capacitación (incluido el conjunto de validación) y esto da el modelo final. Por último, se evalúa el modelo final en el conjunto de pruebas para obtener una estimación del error de generalización.

Esta solución generalmente funciona bastante bien. Sin embargo, si el conjunto de validación es demasiado pequeño, las evaluaciones
del modelo serán imprecisas: se puede terminar seleccionando un modelo subóptimo por error. Por el contrario, si el conjunto de
validación es demasiado grande, el conjunto de entrenamiento restante será mucho más pequeño que el conjunto de entrenamiento
completo. ¿Por qué es esto malo? Bueno, dado que el modelo final se entrenará en el conjunto de entrenamiento completo, no es ideal
comparar modelos candidatos entrenados en un conjunto de entrenamiento mucho más pequeño. Una forma de resolver este problema es realizar repetidas validación cruzada, usando
muchos pequeños conjuntos de validación. Cada modelo se evalúa una vez por conjunto de validación después de haber sido
entrenado en el resto de los datos. Al promediar todo en las evaluaciones de un modelo, se obtiene una medida mucho más precisa de su rendimiento. Sin embargo, hay un
inconveniente: el tiempo de entrenamiento se multiplica por el número de conjuntos de validación.

## Datos incompatibles

En algunos casos, es fácil obtener una gran cantidad de datos para capacitación, peso es probable que estos datos no sean perfectamente representativos (datos diferentes a los que el modelo obtendrá en producción), en este caso la regla más importante es que el conjunto de validación y el conjunto de prueba debe ser lo más representativo posible. Se podrían mezclar los datos representativos con los no representativos pero después de observarlo el rendimiento del modelo en el conjunto de validación es decepcionante. Una solución es mostrar al modelo algunas datos no tan representativos y si funciona bien entonces el modelo no está ajustando demasiado el conjunto de entrenamiento, por el contrario, si el modelo funciona mal en el conjunto de validación, el problema debe provenir de la falta de coincidencia de datos, se puede intentar modificar los datos para que sean más representativos. Por el contrario, si el modelo funciona mal en el conjunto de datos no tan representativos, entonces debe haberse sobrepasado en el conjunto de entrenamiento, por lo que se debe simplificar o regularizar el modelo, obtener más datos de entrenamiento y limpiar los datos de entrenamiento.