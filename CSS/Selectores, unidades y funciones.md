# Selectores, unidades y funciones

## Selectores 

| Patrón                  | Significado                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `*`                     | Cualquier elemento                                           |
| `E`                     | Un elemento de tipo E                                        |
| `E F`                   | Un elemento F que desciende de un elemento E                 |
| `E > F`                 | Un elemento F que es hijo de un elemento E                   |
| `E:first-child`         | Un elemento E cuando E es el primer hijo de su padre         |
| `E:link`                | Un elemento E si E es un enlace y no ha sido visitado        |
| `E:visited`             | Un elemento E si E es un enlace y ha sido visitado           |
| `E:active`              | Un elemento E cuando el elemento es activado por el usuario  |
| `E:hover`               | Un elemento E cuando el cursor del ratón está situado sobre el elemento |
| `E:focus`               | Un elemento E cuando el elemento ha recibido el foco         |
| `E:lang(c)`             | Un elemento E si tiene definido el idioma c                  |
| `E + F`                 | Un elemento F precedido inmediatamente por un elemento E     |
| `E[foo]`                | Un elemento E con el atributo foo con valor(cualquier valor) |
| `E[foo="warning"]`      | Un elemento E con el atributo foo con el valor "warning"     |
| `E[foo~="warning"] `    | Un elemento E con el atributo foo con una lista de valores separado por espacios en blanco, uno de los cuales es exactamente el valor "warning" |
| `E[foo|="en"]`          | Un elemento E con el atributo lang con un valor que comienza con "en" o "en-" |
| `.miClase`              | Un elemento con la clase miClase                             |
| `E.miClase`             | Un elemento E con la la clase miClase                        |
| `#id`                   | Un elemento con el identificador id                          |
| `E#id`                  | Un elemento E con el identificador id                        |
| `E::first-line`         | La primera línea del elemento E                              |
| `E::first-letter`       | La primera letra del elemento E                              |
| `E::before`             | Contenido generado antes del elemento E                      |
| `E::after`              | Contenido generado después del elemento E                    |
| `E[foo^="bar"]`         | Un elemento E que tiene un atributo foo cuyo valor comienza exactamente con la cadena "bar" |
| `E[foo$="bar"]`         | Un elemento E que tiene un atributo foo cuyo valor finaliza exactamente con la cadena "bar" |
| `E[foo*="bar"]`         | Un elemento E que tiene un atributo foo cuyo valor contiene la sucadena "bar" |
| `E:root`                | Un elemento raíz del documento                               |
| `E:nth-child(n)`        | Un elemento E, el hijo n de su padre                         |
| `E:nth-last-child(n)`   | Un elemento E, el hijo n de su padre contando desde el último |
| `:nth-of-type(n)`       | Un elemento E, el hermano n de su tipo                       |
| `E:nth-of-last-type(n)` | Un elemento E, el hermano n de su tipo contando desde el último |
| `E:last-child`          | Un elemento E, el último hijo de se padre                    |
| `E:first-of-type`       | Un elemento E, el primer hermano de su tipo                  |
| `E:last-of-type`        | Un elemento E, el último hermano de su tipo                  |
| `E:only-child`          | Un elemento E, el único hijo de su padre                     |
| `E:only-of-type`        | Un elemento E, el único hermano de su tipo                   |
| `E:empty`               | Un elemento E que no tiene hijos                             |
| `E:target`              | Un elemento E que es el destino de un enlace                 |
| `E:enabled`             | Un elemento E de al interfaz de usuario que está activado    |
| `E:disabled`            | Un elemento E de la interfaz de usuario que está desactiva   |
| `E:checked`             | Un elemento E de la interfaz de usuario que está marcado     |
| `E:not(s)`              | Un elemento E que no cumple el selector simple s             |
| `E ~ F`                 | Un elemento F precedido por un elemento E hermano            |
| `E:in-range`            | Un elemento E de tipo input en el rango                      |
| `E: invalid`            | Un elemento E de tipico input con un valor inválido          |
| `E:optional`            | Un elemento E de tipo input que no tiene el atributo #required |
| `E:out-of-range`        | Un elemento E de tipo input que está fuera de rango          |
| `E:traget`              | Un elemento E activo actual (se hace clic en una URL que contiene el nombre de ancla |
| `E:valid`               | Un elemento E de tipo input con un valor válido              |
| `::selection`           | Texto seleccionado por el usuario                            |

### Ejemplo

~~~css
input[type = "text"]{
    background-color: blue;
}
~~~

## Unidades de medida 

### Unidades relativas de longitud 

| Unidad | Significado                                                  |
| ------ | ------------------------------------------------------------ |
| `em`   | El tamaño calculado del tipo de letra                        |
| `ex`   | La altura de la letra minúscula "x"                          |
| `px`   | Píxel                                                        |
| `%`    | Porcentaje                                                   |
| `rem`  | El tamaño del tipo de letra del elemento raíz                |
| `vw`   | La anchura de la ventana de visualización                    |
| `vh`   | La altura de la ventana de visualización                     |
| `vm`   | El valor menor de la anchura o altura de la ventana de visualización |
| `ch`   | La anchura del cero                                          |

### Unidades absolutas de longitud 

| Unidad | Significado                      |
| ------ | -------------------------------- |
| `in`   | Pulgadas                         |
| `cm`   | Centímetros                      |
| `mm`   | Milímetros                       |
| `pt`   | Puntos (1 punto = 1/72 pulgadas) |
| `pc`   | Picas (1 pica = 12 puntos)       |

### Unidades de ángulos 

| Unidad | Significado       |
| ------ | ----------------- |
| `deg`  | Grado sexagesimal |
| `grad` | Grado centesimal  |
| `rad`  | Radianes          |
| `turn` | Giros             |

### Unidades de tiempo

| Unidad | Significado  |
| ------ | ------------ |
| `ms`   | Milisegundos |
| `s`    | Segundos     |

## Funciones 

`attr()` devuelve el valor del atributo indicado. 

`url()` indica una url para un recurso. 

`counter()` devuelve el valor del contador indicado. 

`calc()` realiza un cálculo aritmético. admite alguno de estos cincos operadores: suma `+`, resta `-`, divisón `/` y módulo de la división `mod`. 