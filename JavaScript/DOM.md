# DOM

Cuando tenemos varias líneas que se refieren al mismo objeto, se utiliza la función `with(objeto){propiedades o metodos}`. Para hacer referencia al objeto `document`, es necesario crear una variable que sea asignada por `document`. 

## Obtener elementos HTML 

Dentro de las etiquetas HTML para hacer referencia a ella en el código de JavaScript se usa la propiedad `id="id"`. Para hacer referencia a el objeto de HTML en JavaScript utilizamos `document.getElementById("elemento");` 

Para las referencias con el nombre del elemento utilizamos `document.getElementsByTagName(nombre).` 

Para las referencias con clases se utiliza `document.getElementsByClassName(class).` 

Para hacer referencia a los formularios en JavaScript se utiliza `document.forms['name']` con el atributo `name="name"`. 

Para hacer referencia a un elemento de un formulario `document.forms['name_form']['name']`. 

Para utilizar los selectores CSS `document.querySelectorAll(selector)`. 

## Cambiar elementos HTML 

`.innerHTML(value)` cambia el código HTML de una página. 

`.attribute` cambia el valor de un atributo. 

`.style` cambia el estilo de un elemento. 

`.setAttribute(atributte, value)` cambia el valor de un atributo. 

## Crear y eliminar elementos HTML 

`document.createElement(element)` crea un elemento HTML 
`document.removeChild(element)` elimina el elemento HTML. 

`document.appendChild(element)` añade un elemento HTML. 

`document.repleaceChild(new, old)` reemplaza un elemento HTML. 

`document.wirte(text)` escribe en la secuencia de salida HTML. 

## Eventos en elementos HTML 

`document.getElementById(id).onclick = function(){code}` 

Para agregar un evento a un elemento se utiliza el método `addEventListener(evento, función, orden)`. 

Para eliminar un evento en un elemento se utiliza `.removeEventListener(evento, función)`. 