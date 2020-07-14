# Ecuaciones del Machine Learning

## Error cuadrático medio

_Root Mean Square Error (RMSE)_
$$
RMSE(X,h)=\sqrt{\frac{1}{m}\sum_{i=1}^{m} (h(X^{(i)})-y^{(i)})^2}
$$

- $m$ número de instancias en el dataset.

- $X^{(i)}$ es un vector de todos los valores de características (excluyendo la etiqueta) de la instancia $i^{th}$ en el dataset, y $y^{(i)}$ es su etiqueta (el valor de salida deseado para esa instancia).

- $X$ es una matriz que contiene todos los valores de características (excluyendo etiquetas) de todas las instancias en el conjunto de datos. Hay una fila por instancia y la fila $i^{th}$ es igual a la transposición de $X^{(i)}$, anotado $(X^{(i)})^T$.
  $$
  X=\left(\begin{array}{cc} 
  (X^{(1)})^T \\
  (X^{(2)})^T \\
  ... \\
  (X^{(1999)})^T \\
  (X^{(2000)})^T \\
  \end{array}\right)=
  \left(\begin{array}{cc}
  -118.29 & 33.91 1416 & 38372 \\
  ... & ... & ...
  \end{array}\right)
  $$

- h es la función de predicción del sistema, también llamada hipótesis. Cuando el sistema recibe el vector de características de una instancia $X^{(i)}$ genera un valor predicho $\hat{y}^{(i)} = h(X^{(i)})$ para esa instancia ($\hat{y}$ se pronuncia "y-hat").
- $RMSE(X, h)$ es la función d ecosto medida en el conjunto de ejemplos usando su hipótesis $h$.

## Error absoluto medio

Mean absolute error (MAE)
$$
MAE(X,h)=\frac{1}{m}\sum_{i=1}^{m}|h(X^{(i)}) - y^{(i)}|
$$
