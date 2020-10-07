# Vectores

La forma básica de construir vectores es usando el comando `c()`.

~~~R
x <- c(2,3,0,3,1,0,0,1)
#Para imprimir x solo se escribe x
~~~

El operador `<-` es el operador de asignación.

## Acceder a los elementos

`x[3]` tercer elemento.

`x[2:5]` rango de elementos.

`x[-2]` todos los elementos salvo uno en particular.

`x[x > 1]` elementos que cumplan alguna condición.

## Creación de vectores

`x<-1:10` rango de enteros.

`x<-seq(1, 10, by=2)` rango de enteros con intervalo.

`x<-rep(5,3)` número repetido varias veces.

## Concatenar

Se pueden concatenar vectores utilizando la misma función `c()`.

~~~R
T = c(T, 10)
~~~