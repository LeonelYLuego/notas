# JQuery

La librería JQuery se puede agregar de dos maneras, la primera es por medio de los servidores en la web agregando en el código de HTML lo siguiente: 

`<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>`

La otra manera es descargando la librería e incluyéndola en el archivo HTML.  

## Selectores 

| Selector                                                  | Sintaxis                           |
| --------------------------------------------------------- | ---------------------------------------- |
| Elemento                                                  | `$("element")`                           |
| Id                                                        | `$("#id")`                               |
| Clase                                                     | `$(".class")`                            |
| Todos los elementos                                       | `$("*")`                                 |
| Elemento actual                                           | `$("this")`                              |
| Elemento con la clase                                     | `$("element.class")`                     |
| Primer elemento                                           | `$("element:first")`                     |
| El primer elemento del elemento                           | `$("element1 element2:first")`           |
| Todos los elementos con el atributo                       | `$("[attribute]")`                       |
| Elemento con el atributo igual a lo indicado              | `$("element[attribute = 'something']")`  |
| Elemento con el atributo diferente a lo indicado          | `$("element[attribute != 'something']")` |
| Elementos pares                                           | `$("element:even")`                      |
| Elementos impares                                         | `$("element:odd")`                       |
| Todos los elementos y todos los elementos con el atributo | `$(":element")`                          |

## Efectos 

| Propiedad                                     | Se refiere a                                                 | Valores que admite                     |
| --------------------------------------------- | ------------------------------------------------------------ | -------------------------------------- |
| `.hide()`                                     | Oculta un elemento.                                          | `slow`, `fast`                         |
| `.show()`                                     | Muestra un elemento.                                         | `slow`, `fast`                         |
| `.toggle`                                     | Alterna entre mostrar y ocultar un elemento.                 | Ninguno                                |
| `.fadeIn()`                                   | Muestra un elemento desvaneciéndose.                         | `slow`, `fast`, milisegundos, ninguno. |
| `.fadeOut()`                                  | Oculta un elemento desvaneciéndose.                          | `slow`, `fast`, milisegundos, ninguno. |
| `.fadeToggle()`                               | Alterna un elemento para desvanecerlo.                       | `slow`, `fast`, milisegundos, ninguno. |
| `.html()`                                     | Sustituye código html y te regresa el código en él.          | Código a poner, ninguno.               |
| `.text()`                                     | Sustituye texto sin utilizar etiquetas html.                 | Código a poner.                        |
| `.val()`                                      | Sustituye u obtiene el valor del form.                       | Valor a poner, ninguno.                |
| `.attr()`                                     | Obtiene el valor de un atributo.                             | Atributo, valor.                       |
| `.after()`                                    | Agrega código después del elemento.                          | Código a poner.                        |
| `.append()`                                   | Agrega código después del que hay dentro del elemento.       | Código a poner.                        |
| `.prepend()`                                  | Agrega código antes del que hay dentro del elemento.         | Código a poner.                        |
| `.before()`                                   | Agrega código antes del elemento.                            | Código a poner.                        |
| `.slideDown()`                                | Despliega hacia abajo.                                       | `slow`, `fast`, milisegundos, ninguno. |
| `.slideUp()`                                  | Despliega hacia arriba.                                      | `slow`, `fast`, milisegundos, ninguno. |
| `.slideToggle()`                              | Despliega hacia arriba y abajo.                              | `slow`, `fast`, milisegundos, ninguno. |
| `.animatw({parametros}, velocidad, callback)` | Animación.                                                   | `{ left: '250px´, height: '+=10px'}`   |
| `.stop()`                                     | Detiene una animación.                                       |                                        |
| `.remove()`                                   | Elimina un elemento.                                         | Selector de los elementos a eliminar.  |
| `.empty()`                                    | Elimina todos los hijos de un elemento.                      | Ninguno.                               |
| `.addClass()`                                 | Añade el atributo clase.                                     | Clase.                                 |
| `.removeClass()`                              | Eliminar el atributo clase.                                  | Clase.                                 |
| `.toggleClass()`                              | Añade o elimina el atributo clase.                           | Clase.                                 |
| `.css()`                                      | Cambia las propiedades CSS o regresa las propiedades.        | Propiedad, valor.                      |
| `.width()`                                    | Obtiene o cambia la anchura de un elemento.                  | Dimensión.                             |
| `.height()`                                   | Obtiene o cambia la altura de un elemento.                   | Dimensión.                             |
| `.innerWidth()`                               | Obtiene o cambia la anchura de un elemento incluyendo el padding. | Dimensión.                             |
| `.innerHeight()`                              | Obtiene o cambia la altura de un elemento incluyendo el padding. | Dimensión.                             |
| `.outerWidth()`                               | Obtiene o cambia la anchura de un elemento incluyendo el padding y border. | Dimensión, true para incluir margin.   |
| `.outerHeight()`                              | Obtiene o cambia la altura de un elemento incluyendo el padding y border. | Dimensión, true para incluir margin.   |
| `.parent()`                                   | Obtiene el padre del elemento.                               | Ninguno.                               |
| `.parents()`                                  | Obtiene todos los padres del elemento.                       | Ninguno.                               |
| `.parentsUntil()`                             | Obtiene todos los padres hasta el elemento dado.             | Selector de elemento.                  |
| `.children()`                                 | Obtiene todos los hijos del elemento.                        | Ninguno.                               |
| `.find()`                                     | Obtiene todos los elementos hasta el elemento dado.          | Selector de elemento.                  |
| `.siblings()`                                 | Obtiene todos los hermanos del elemento o los elementos dados. | Ninguno, selector de elemento.         |
| `.next()`                                     | Obtiene el siguiente elemento hermano.                       | Ninguno.                               |
| `.nextAll()`                                  | Obtiene todos los elementos hermanos siguientes.             | Ninguno.                               |
| `.nextUntil()`                                | Obtiene todos los elementos hermanos siguientes hasta el elemento dado. | Selector de elemento.                  |
| `.prev()`                                     | Obtiene el elemento hermano anterior.                        | Ninguno.                               |
| `.prevAll()`                                  | Obtiene todos los elementos hermanos anteriores.             | Ninguno.                               |
| `.prevUntil()`                                | Obtiene todos los elementos hermanos anteriores hasta el elemento dado. | Selector de elemento.                  |
| `.first()`                                    | Obtiene el primer elemento.                                  | Ninguno.                               |
| `.last()`                                     | Obtiene el último elemento.                                  | Ninguno.                               |
| `.eq()`                                       | Obtiene el elemento con el índice especificado.              | Índice.                                |
| `.filter()`                                   | Obtiene los elementos que coinciden con el selector dado.    | Selector de elemento.                  |
| `.not()`                                      | Obtiene los elementos que no coincidan con el selector dado. | Selector de elemento.                  |

Las transiciones se ejecutan en segundo plano, para evitar errores se puede pasar como parámetro una función para que se ejecute después de la transición. 

Cuando se seleccionan varios elementos, para acceder a ellos individualmente se utiliza el subíndice. 

## Eventos 

Son similares a los eventos de JavaScript pero sin el prefijo "on". 

Para utilizar los eventos: 

~~~javascript
$("p").click(function(){
    //...
});
~~~

El método `on()` permite agregar varios eventos en un solo elemento. 

## Cargar una página 

Un código muy utilizado con JQuery es el de que al terminar de cargar una página, esta haga lo que necesitamos y no lo haga justo antes de mostrar el contenido de la página. 

~~~javascript
$(document).ready(function(){
    //código a ejecutar.
});
~~~