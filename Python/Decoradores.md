# Decoradores

Un decorador es una función que recibe como argumento una función y la ejecuta antes o después de las operaciones que deseemos agregar, retornando la función para que nosotros la ejecutemos, su sintaxis es la siguiente:

~~~python
def my_decorator(function):
    #Funciones anidadas
    def new_fuction(*args, **kwargs): #Recibe cualquier parámetro
        #Operaciones antes de la funcion
        value = function(*args, **kwargs) #Se llama a la funcion con sus argumentos
        #Operaciones después de la funcion
        return value #regresamos el valor retornado por la función
    return my_decorator
~~~

Para utilizar el decorador:

~~~python
@decorator
def my_fuction():
	#operaciones a realizar
~~~