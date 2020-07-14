# Cookies, Sesiones, Filtros

## Cookies 

Las cookies son utilizadas para identificar a los usuarios. Para crear una cookie se utiliza la función `setcookie(nombre, valor, caducidad, ruta, dominio, seguro, httponly)`, sólo el nombre es un parámetro requerido.

Para saber si se ha establecido una cookie se utiliza `isset($_COOKIE[$cookie_name])` y para obtener su valor con `$_COOKIE[$cookie_name]`. 

Si se quiere eliminar un cookie se pone una fecha que ya halla pasado. 

## Sesiones

Las variables de sesión guardan la información que va a ser usada en varias páginas, por defecto las variables de sesión duran hasta que el usuario cierra el navegador. 

Una sesión se inicia con la función `session_start()`, esta debe ser la primera cosa en el documento antes de las etiquetas HTML, y debe ir en todos los documentos que queramos utilizar las variables de sesión. 

Para obtener, añadir o modificar variables de sesión se utiliza la variable global `$_SESSION["nomre_variable"]`. 

Para destruir todas las variables de sesión se utiliza `session_unset()` y para destruir la sesión se utiliza `session_destroy()`; 

## Filtros 

Los filtros sirven para ver si una entrada de usuario es válida o no, para ellos podemos visitar la página: https://www.w3schools.com/php/php_filter.asp 