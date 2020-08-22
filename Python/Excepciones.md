# Excepciones

Las excepciones son errores que ocurren fuera de nuestras manos, cuando se está ejecutando el programa y ocurre algún error que el programa no esperaba, si esto sucede y no tenemos un manejo de estos errores entonces el programa terminará repentinamente en donde se estaba ejecutando y causará un problema al usuario final. Para intentar ejecutar un código con la posibilidad de que ocurra algún error utilizamos:

~~~python
try:
	#código
~~~

Para tratar este error utilizamos la palabra:

~~~python
except Exception:
	#código
~~~

Esta última debe contener el nombre del error, y si es un error genérico utilizamos la clase Exception. Podemos renombrar el tipo de error:

~~~python
except Exception as ex:
	print(ex) #se imprime le porque del error
~~~