# 	Manejo de datos

## Datos tipo I

Los datos en R se pueden representar en vectores.

~~~r
x <- c(1,2,3,1,2,4,2,2,3,3,2,4,4)
~~~

Cuando son pocos datos, se pueden trabajar con ellos en forma extensiva.

## Datos tipo II

En algunas ocasiones es mejor trabajar con los datos utilizando tablas de frecuencia.

~~~R
table(chickwts$feed)
~~~

Se pueden dividir los datos en base a una variable.

~~~R
Wsep <- split(chickwts$weight, chickwtd$feed)
~~~

~~~R
table(chickwts$feed) #Tabla de frecuencia
mean(chickwts$weight) #Promedio de los pesos de los pollos
mean(chcikwts$weight[chickwts$feed=="horsebean"]) #peso para los pollos que usarin el alimento horsebean
Wsep <- split(chickwts$weight, chickwts$feed) #Promedios de los pesos para lo diferentes tipos de alimento, separar los datos en base a esa variable
mean(Wsep$horsebean) #Obtener el promedio
sapply(Wsep,mean) #medias de los pesos por tipo de alimento
~~~

## Datos tipo III

Si el número de posibles valores es muy grande, convine tal vez mejor agruparlos por intervalos.

~~~R
ruta <- file.choose()
x <- read.table(ruta, sep=",", header=TRUE)
I <- cut(x$Age, c(20, 30, 40, 50, 60, 70, 80, 90))
table(I)
~~~

