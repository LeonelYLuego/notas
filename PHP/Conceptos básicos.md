# Conceptos básicos

Para agregar código PHP en una página web se crea un bloque: 

~~~php
<?php
    
?>
~~~

Los comentarios se escriben `//`, `#`, `/* */`. 

Para crear y utilizar una variable se utiliza la sintaxis: 

`$variable = 10;` 

si se quiere crear una variable global en un punto local se utiliza la palabra reservada `global`. La palabra `static` hace que una variable no se destruya cuando es local. 

Para definir una constante sigue la siguiente sintaxis: `define(name, value, case-insensitive)`, donde `case-insensitive` dice si la variable debe ser sensible a las mayúsculas. 

En php el `else if` es `elseif`. 

En un array podemos crear un bucle en el cual una variable tome todos los valores del array: `foreach($array as $value)`. 