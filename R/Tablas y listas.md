# Tablas y listas

## Listas

Se puede crear una lista con la función `lsit()` pasándole como parámetro el nombre de cada columna y los valores.

~~~R
tiempos <- list("Shell" = tS, "Quick" = tQ, "Radix" = tR)
~~~

## Tablas

Una tabla se puede crear utilizando la función `table()`, esta se convierte en una tabla de frecuencias.

~~~R
T <- table(x$peticion)
~~~

Se pueden realizar operaciones directamente con la tabla.

~~~R
fk <- T/sum(T)
pr <- fk * 100
~~~

Las tablas se pueden unir por columnas `cbind`, o por filas `rbind`.

~~~R
Tabla <- cbind(T, fk, pr)
~~~

