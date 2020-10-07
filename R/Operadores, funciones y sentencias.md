# Operadores, funciones y sentencias

## Sentencias de control

`ifelse` condicional

~~~R
sons <- ifelse(x$sonscount > 0, "Yes", "No")
~~~

`for` bucle finito.

~~~R
for(i in 1:100){
    print(i)
}
~~~

## Funciones

`exp(x)` exponencial de cada uno de los elementos del vector.

`x^2` cuadrado de todos los elementos del vector.

`x + 1` sumar 1 a todos los elementos del vector.

En estos casos, el resultado es un vector resultado de aplicar la función a cada elemento del vector.

`runif(n)` crea un vector de n con valores aleatorios entre 0 y 1.

`Sys.time()` obtiene la hora del sistema.

`sort(x)` ordena el vector.

- `method` selecciona el método de ordenamiento.
  - `"shell"`
  - `"quick"`
  - `"radix"`
  - `"auto"`

### Operadores

`sum(x)` suma de los elementos del vector.

`mean(x)` media de los elementos del vector.

`median(x)` mediana del vector.

`var(x)` varianza de los elementos del vector (la dividida entre n - 1).

`max(x)` valor máximo de los elementos del vector.

`quantile(x, 0.73)` El cuantil 0.73 (es decir, Cp para p=0.73) de los datos.

`length(x)` número de elementos en x.

`lapply(x, operator)` obtiene una tabla aplicacando el operador a cada columna.

- mean
- sd

#### Ejemplos

`sum(x^2)` suma de los cuadrados de los elementos del vector.

 `sqrt(var(x))` desviación estándar.

`sum(x) / length(x)` otra forma de calcular la varianza.