# String

Los string en Python se pueden declarar con `' '` o `" "` y para crear un string con saltos de línea se utiliza `""" """`. 

## Métodos

### Concatenar

`new_string = my_string_one + ' ' + my_string_two`

`new_string = "%s %s" %(my_string_one, my_string_two) `

`new_string = "{} {}".format(my_string_one, my_string_two)`

`new_string = "{b} {a}".format(a = my_string_two, b = my_string_one)`

### Mayúsculas y minúsculas

`my_string.lower()` minúsculas.

`my_string.upper()` mayúsculas.

`my_string.title()` mayúscula al principio de cada palabra.

### Buscar, contar, reemplazar

`position = my_string.find("Hello")`

`count = my_string.count("o")` cuenta cuantas veces se encuentra.

`new_string = my_string.replace('o', 'x')`

### Separar por un carácter

`new_list = my_string.split(' ')`