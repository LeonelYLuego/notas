# Posicionamiento

## Display 

`display:` define el tipo de visualización para un elemento en una página web. El tipo de visualización se define indicando el tipo de caja del elemento. Existen más de 20 valores para esta propiedad, pero los más comunes son: 

- `block` el elemento se comporta como un elemento de bloque, como `<div></div>`. 
- `inline` el elemento se comporta como un elemento en línea, como `<span></span>`. 
- `inline-block` se posiciona como un elemento inline, pero se comporta como un block. 
- `table` el elemento se comporta como una tabla. 
- `none` el elemento no se visualiza y no participa en la maquetación de la página, se utiliza para ocultar elementos y luego aparecer. 

`visibility:` propiedad que oculta los elementos, pero sigue ocupando un espacio, al contrario que `display: none;` que no ocupa un espacio. 

- `hidden`
- `visible`

## Position

`position:` especifica el tipo de posicionamiento de un elemento. Esta propiedad puede tomar los siguientes valores: 

- `static` el elemento se posiciona según su orden de aparición en el flujo de la página, es el valor por defecto. 
- `relative` el elemento se posiciona de forma relativa a su posición normal. `top`, `bottom`, `left` y `right` harán que se pueda ajustar fuera de su posición normal. Otro elemento no se puede ajustar para adaptarse a cualquier hueco dejado por el elemento. 
- `absolute` el elemento se posiciona de forma relativa a su primer antecesor posicionando con un valor distinto de `static`. 
- `fixed` el elemento se posiciona de forma relativa a la ventana del navegador (no se mueve con el cursor). 
- `sticky` el elemento alterna entre `fixed` y `relative`, cuando está dentro de la ventana se desplaza junto con el cursor y cuando va a salir de la ventana se queda fijo en un punto y ya no se mueve con el cursor. Es necesario especificar top, `bottom`, `left` o `right`. 

`z-index:` especifica el orden de apilamiento de un elemento, puede tener un valor positivo o negativo, se puede utilizar con `absolute`. 

## Float

`float:` indica si una caja debe flotar a la izquierda, a la derecha o no debe flotar en absoluto. Esta propiedad se puede emplear con cajas que no están posicionadas absolutamente. Esta propiedad puede tomar los siguientes valores: 

- `left` la caja flota a la izquierda. El contenido fluye sobre el costado derecho de la caja, comenzando en la parte superior.
- `right` la caja flota a la derecha. El contenido fluye sobre el costado izquierdo de la caja, comenzando en la parte superior.
- `none` la caja no es flotante.
- `inherit` hereda el valor flotante de su padre.

Además para anular el efecto de una caja flotante existe la propiedad `clear`, especifica qué elementos de propiedad puede flotar junto al elemento de aclarado y de que lado. Esta propiedad puede tomar los siguientes valores: 

- `left` la caja generada se mueve debajo de todas las cajas flotantes a la izquierda, los elementos flotantes no se permiten en el lado izquierdo. 
- `right` la caja generada se mueve debajo de todas las cajas flotantes a la derecha, los elementos flotantes no se permiten en el lado derecho. 
- `both` la caja generada se mueve debajo de todas las cajas flotantes que aparecen antes del documento, no se permiten elementos flotantes en la izquierda ni en la derecha. 
- `none` no se aplica ninguna restricción a la posición de la caja con respecto a las cajas flotantes que pueden existir, permite que los elementos floten en ambos lados. 
- `inherit` hereda el valor flotante de su padre. 

Si un elemento es más alto que el elemento que lo contiene, y que se hace flotar, hará un desbordamiento fuera de su contenedor, entonces podemos añadir `overflow: auto;` al elemento que contiene para solucionar este problema. 

## Overflow 

`overflow:` especifica si se recorta el contenido o añadir barras de desplazamiento cuando el contenido de un elemento es demasiado grande para caber en el área especificada. La propiedad solo funciona para elementos de bloque con una altura especificada. 

- `visible` el desbordamiento no se recorta. El contenido sale fuera de la caja del elemento. 
- `hidden` el desbordamiento se recorta, y el resto del contenido será invisible. 
- `scroll` el desbordamiento se recorta y se agrega una barra de desplazamiento para ver el esto del contenido. 
- `auto` similar a `scroll`, pero añade una barra de desplazamiento sólo cuando sea necesario. 

La propiedad existe para los dos ejes: `overflow-x` y `overflow-y`. 