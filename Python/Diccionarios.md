# Diccionarios

Un diccionario en Python es como una lista, pero en vez de que los subíndices sean valores enteros desde el valor 0 hasta el valor (n_elementos – 1) el subíndice lo podemos indicar nosotros. Para declarar un diccionario se hace de la siguiente forma: 

~~~pyth
my_dictionary = {'a':25, 'b':True, 'c':'Hello'}
~~~

Las claves deben de ser inmutables.

## Métodos

### Establecer un valor

`my_dictionary['a'] = 30` modifica el valor de la llave.

`my_dictionary['z'] = 'bye'` crea una nueva llave con su valor.

### Obtener un valor

`new_value = my_dictionary['a']` obtiene el valor de la llave sin comprobación.

`new_value = my_dictionary.get('z', False)` obtiene el valor de la llave y en caso de no encontrarla te regresa el segundo atributo.

### Eliminar un valor

`del my_dictionary['a']` elimina el valor y la llave.

### Obtener un objeto iterable

`my_dictionary_keys = my_dictionary.keys()` objeto iterable con las llaves.

`my_dictionary_values = my_dictionary.values()` objeto iterable con los valores.

`my_dicitionary_items = my_dictionay.items()` objeto iterable con los valores y las llaves. 

### Concatenar diccionarios

`my_dictionary.update(my_dictionary_two)` agrega los valores del diccionario de argumento al diccionario.