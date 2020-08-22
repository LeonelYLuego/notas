# Listas

Las listas en Python se ponen entre ` []` y se declaran de la siguiente forma:

~~~python
my_list = [2, “Tres”, True, [“Uno”, 10]]
~~~

Una lista es un array dinámico que puede almacenar cualquier tipo de valor.

## Métodos

### Obtener valores

`my_list[0]` accede al subíndice indicado.

`new_list = my_list[0:4:2]` [valor inicial, cuantos valores se tomarán, salto].

### Agregar valores

`my_list[0:2] = [4, 3]` agregar estos valores a la lista.

`my_list.append(“hello”)` agregar al final el valor entre paréntesis.

`my_list.insert(1, “insert”)` agregar en la posición el valor.

### Eliminar valores

`my_list.remove(“hello”)` eliminar el valor.

`last_value = my_list.pop()` eliminar el ultimo valor y obtenerlo.

### Concatenar listas

`my_list.extend(my_list_two)` #Agregar a la lista la segunda lista.

### Ordenar lista

`my_list.sort()` menor a mayor.

### Convertir un valor a una lista

`list(value)`