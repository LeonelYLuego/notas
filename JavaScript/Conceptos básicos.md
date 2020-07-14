# Conceptos básicos

## Incluir código JavaScript en una página 

El código de un `script` se puede incluir en 3 lugares: 

- `<head>` se agrega en esta sección con la etiquete `<script>` y se ejecuta antes de que cargue la página. 
- `<body>` se agrega en esta sección con la etiqueta `<script>` y se ejecuta hasta el final de la carga de la página. 
- `<script src=""><script>` incluye un fichero de código externo. 

## Salida 

Se puede visualizar los resultados del `script` en diferentes lugares: 

- `innerHTML()` dentro de un elemento HTML. 
- `document.write()` dentro del documento HTML, si se utiliza después del que el documento allá cargado, se eliminará todo el código HTML. 
- `window.alert()` dentro de una alerta del navegador. 
- `console.log()` dentro de la consola del navegador. 

## Sintaxis 

Números: `10`, `10.36`. 

Cadenas de caracteres: `"Hola"`, `'hola'`. 

Variables: `var x = undefined;` 

Comentarios: `//`, `/* */`. 

Array: `var cars = ["Saab", "Volvo", "BMW"]`. 

Objectos: `var object = {name:"", age:""};`. 

## Modo estricto 

El modo estricto es utilizado para que el código sea más riguroso con la sintaxis del mismo. Para activarlo utilizamos `"use strict";`. 

## Cargar un archivo después de cargar una página

~~~html
<script>
    window.onload = function() {
        var element = document.createElement("script");
        element.src = "myScript.js";
        document.body.appendChild(element);
    };
</script>
~~~