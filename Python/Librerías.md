# Librerías

### random

~~~python
randint(0, 10) #obtiene un valor del 0 al 10
choice(my_list) #devuelve un valor de la lista
shuffle(my_list) #desordena la lista
~~~

### datetime

~~~python
datetime.now() #obtiene la fecha y hora actual
~~~

### time

~~~python
sleep(0.5) #retardo de medio segundo
~~~

### sys

~~~python
stdout.write(“\r%d %%” %i) #escribe en la consola
stdout.flush() #refresca la consola para poder escribir de nuevo
~~~

#### Argv

Cuando ejecutamos una aplicación por consola, esta puede recibir varios parámetros los cuales nosotros podemos obtener mediante la librería sys, esto nos ayuda a ejecutar la aplicación de la manera que el usuario solicita sin tener que recibir una entrada.

~~~python
import sys
print(sys.argv) #nos devuelve una lista con los parámetros pasados al intentar ejecutar la función
~~~