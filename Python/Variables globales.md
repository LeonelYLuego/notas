# Variables globales

Las variables globales se crean automáticamente siempre y cuando estén fuera de cualquier función, pero para utilizarla dentro de una función solo se podrá obtener el valor de ella o se deberá utilizar la palabra reservada “global” para poder modificarla.

~~~python
global_variable = "Un valor"

def my_fuction():
    global global_variable
    global_variable = "Modificamos el valor de la variable"
~~~

Para crear una variable global dentro de una función se hace de la misma manera que se muestra arriba.

**Nota:** para utilizar una variable global dentro de una función es necesario primero declarar antes de utilizarla a menos que la vayamos a declarar dentro de la función.