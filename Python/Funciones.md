# Funciones

Para declarar una función se hace de la siguiente manera:

~~~python
def my_fuction(lista de parámetros que pueden ser por omisión):
	#operaciones
~~~

## Documentar una función

Es una buena práctica documentar las funciones para que así cuando nosotros o más personas queramos saber lo que hace esa función podamos obtener esa información de una manera más rápida y sencilla de entender.

Para agregarla debemos declarar la función, y en la primera línea después de la declaración entre 3 comillas dobles colocamos la información que queremos que sepa la otra persona.

~~~python
def my_fuction(*args): 
	"""Función demostrativa"""
	#operaciones
~~~



Para obtener la documentación se utilizan las funciones:

~~~python
print(my_fuction.__doc__) #Obtenemos la descripción 
print(my_fuction.__name__) #Obtenemos el nombre de la función 
~~~

O si se importa la función dentro del intérprete de Python:

~~~python
from my_program import my_fuction
help(my_fuction)
~~~

 

## Múltiples argumentos

Cuando no sabemos cuántos argumentos nos pasaran en la llamada de una función se puede declarar el argumento como `*args`:

~~~python
def my_fuction(*args): #Esto nos regresará una tupla de los argumentos que fueron pasados
    #operaciones

my_fuction(10, 20, 30) #Llamada a la función
~~~



Y cuando queremos que dentro de los argumentos de una función estos tengan una llave, se declara el argumento de la función con `*kwargs`:

~~~python
def my_fuction(*kwargs): #Nos regresará un diccionario
	#operaciones

my_fuction(valor = ‘Hola’, x = 20, y = True) #Llamada a la función
~~~



## Funciones dentro de funciones

Se pueden crear funciones dentro de funciones con el propósito de utilizar esas funciones dentro de la otra función:

~~~python
def my_fuction(lista de argumentos):
    #operaciones
    def my_second_fuction(): #Los argumentos pasados en la primera función también podrán ser utilizados en esta
~~~



 También se puede regresar una función ya creada denominada *closure*:

~~~python
def my_fuction(lista de argumentos):
    #Operaciones de la primera función
    def my_second_function():
    	#Operaciones de la segunda función
    return my_second_fuction

new fuction = my_fuction(values)
my_fuction() #No es necesario colocar los argumentos que fueron ya pasados para crear la función

~~~