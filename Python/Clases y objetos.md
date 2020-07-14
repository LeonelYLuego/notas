# Clases y objetos

Una clase es la estructura de un objeto, se declara:

~~~python
class MyClass:
	#Atributos, métodos
~~~

### Atributos y métodos

Los atributos son todas aquellas propiedades o características que tiene el objeto, normalmente suelen ser variables y los métodos son todas las acciones que realiza el objeto. Se declara:

~~~python
class MyClass:
	#Atributos
	my_attribute = None

    #Métodos
	def my_method(self):
		#operaciones
		return self.my_attribute
~~~

### Instanciar la clase

~~~python
my_object = MyClass()
~~~

### Constructor

Para crear el constructor de un objeto (método que se ejecuta al momento de crear un objeto) utilizamos la función `__init__` con los parámetros que queramos:

~~~python
class MyClass:
	def __init__(self, attribute):
	self.my_attribute = attribute
~~~

Entonces al momento de querer instanciar la clase, se escribiría de la siguiente manera:

~~~python
my_object = MyClass("Un valor")
~~~

### Atributos y métodos privados

Para crear métodos y atributos privados dentro de una clase sólo es necesario poner dos caracteres de subrayado antes del identificador:

~~~python
class MyClass:
    __my_attribute = None #atributo privado
	def __my_method(self): #método privado
        #operaciones
~~~

### Variable estática

Existen un tipo de variable que podemos utilizar dentro de todos nuestros objetos y siempre estará inicializada con un valor, e incluso podremos acceder a ella sin la necesidad de tener un objeto creado, esto se le conoce como *variable de clase*, en otros lenguajes sería una variable declarada de tipo estática:

~~~python
class MyClass:
	_pi = 3.1416
~~~

### Decorador property

Para obtener y modificar un atributo declarado privado dentro de una clase podemos utilizar los decoradores propeties de la siguiente manera:

~~~python
class MyClass:
    @property
    def my_attribute(self):
    	return self.__my_attribute
    @my_attribute.setter
    def my_attribute(self, value):
    	self.__my_attribute = value
~~~

### Métodos estáticos

Los métodos estáticos son aquellos métodos que no necesariamente tenemos que crear un objeto para poder utilizarlos, para crearlos lo utilizamos un decorador:

~~~python
class MyClass:
    @staticmethod
    def pi():
    	return 3.1416
~~~

Para utilizar los métodos estáticos fuera de un objeto, solo ponemos el nombre de la clase seguido de un punto y el nombre del método con sus debidos parámetros y dentro de la clase podemos poner la palabra reservada self seguida del método o igual que si no hubiera objeto.

~~~python
self.pi() #dentro de la clase

MyClass.pi() #fuera de la clase
~~~