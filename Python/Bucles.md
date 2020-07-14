# Bucles

# while

#### Ejemplo:

~~~python
while value < 10:
	#código
else: #si ya no se cumple la condición entonces ejecuta esta parte
	#código 
~~~

# For

El for se trabaja diferente que, en otros lenguajes de programación, su declaración es la siguiente:

```python
for [variable o variables] in [rango o valores que va a tomar]:
    #operaciones
```

#### Ejemplos:

`for value in my_list:` se guarda en value todos los valores de la lista.
`for value in range(0, 20, 4):` value va desde 0 a 19 con salto de 4.
`for index, value in in enumerate(my_list):` nos regresa el índice y valor de la lista.
`for value in range(0, len(my_list)):` for que va desde el valor 0 hasta el número de elementos.
`for value in range 'hola mundo':` value pasa por todos los caracteres de la cadena.
`for index, value in my_dictionary.items():` regresa índice y los valores de los índices.