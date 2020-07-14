# Objetos de HTML

## Texto 

Para poder modificar el estilo de un texto utilizamos: 

~~~javascript
identificador.style.propiedad = valor;
~~~

Propiedades relativas del texto 

| Propiedad           | Actúa sobre                                                  | Valores que admite                                           |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `backgroundColor`   | Color de fondo.                                              | Un color, como nombre o como notación hexadecimal.           |
| `backgroundImage`   | Imagen de fondo.                                             | La ruta y nombre de archivo que contiene una imagen válida.  |
| `border`            | Los bordes del párrafo                                       | Las especificaciones del borde.                              |
| `borderBottomColor` | El color del borde inferior del párrafo.                     | Un nombre de color o su representación hexadecimal.          |
| `borderBottomStyle` | El tipo de borde inferior del párrafo.                       | Los posibles valores son `inset`, `groove`, `double` y `solid`. |
| `borderBottomWidth` | El espesor del borde inferior del párrafo.                   | `thick`, `thin` o un valor seguido de px o cm.               |
| `borderColor`       | El color del borde.                                          | Un nombre de color o su valor hexadecimal.                   |
| `borderStyle`       | El tipo de borde del párrafo.                                | Los posibles valores son `inset`, `groove`, `double` y `solid`. |
| `borderWidth`       | El espesor del borde del párrafo                             | `thick`, `thin` o un valor seguido de px o cm.               |
| `color`             | El color del texto.                                          | Un nombre de color o su valor hexadecimal.                   |
| `filter`            | Establece un filtro CSS.                                     | Cualquier filtro CSS válido.                                 |
| `fontFamily`        | La tipografía del párrafo de texto.                          | Uno o más nombres de fuentes.                                |
| `fontSize`          | El tamaño de la fuente del párrafo.                          | `xx-small`, `x-small`, `small`, `medium`, `large`, `x-large`, `xx-large`, o un valor númerico. |
| `fontStyle`         | Letra cursiva.                                               | `italic` u `oblique`, `normal`.                              |
| `fontVariant`       | Párrafo en letra VERSALLES.                                  | `normal` o `small-caps`.                                     |
| `fontWeight`        | El espesor de la letra.                                      | `lighter`, `light`, `normal`, `bold`, `bolder`, `100`, `200`, ... , `900`. |
| `letterSpacing`     | Determina el espaciado entre letras.                         | Un valor, seguido de una unidad de medida.                   |
| `textAlign`         | La alineación horizontal del texto en su ubicación.          | `left`, `center`, `right`, `justify`.                        |
| `textDecoration`    | Decoración del texto.                                        | `none`, `blink`, `underling`, `overline`, `line-trought`.    |
| `textIdent`         | Sangría de la primera línea respecto al resto del párrafo.   | Un valor seguido de una unidad de medida.                    |
| `textTransform`     | Determina si la letra aparece en mayúsculas, minúsculas o en mayúsculas la primera de cada palabra. | `uppercase`, `lowercase`, `capitalize`.                      |

### Ejemplos: 

`id.style.color = "#ff0000";` cambia el color de un texto. 

`id.style.fontFamily = "Arial";` cambia el tipo de letra de un texto. 

`id.style.fontSize = "13px";` cambia el tamaño de letra de un texto. 

`id.style.background = "#ff0000";` cambia el color de fondo de un texto. 

`id.style.textAlign = "center";` 

## Imágenes 

Las imágenes dentro de una página web se guardan mediante una referencia en una matriz llamada `document.images`, para saber si la página tiene imágenes utilizamos la propiedad `document.images.length` que nos regresa el número de imágenes y para acceder a una imagen lo hacemos como una matriz `document.images[0]` o se puede acceder por la propiedad name de la etiqueta HTML `document.images.["name"]`. 

 

Propiedades del objeto image 

| Propiedad  | Se refiere a                                                 |
| ---------- | ------------------------------------------------------------ |
| `border`   | Determina el grosor del borde que rodea a la imagen. Es de lectura y escritura. |
| `complete` | Esta propiedad devuelve un valor lógico que será false si la imagen no se ha cargado del todo o true, si ya está completamente cargada. Es de sólo lectura. |
| `hspace`   | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es de lectura y escritura. |
| `height`   | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es de lectura y escritura. |
| `lowsrc`   | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es de lectura y escritura. |
| `name`     | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es sólo de lectura. |
| `src`      | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es de lectura y escritura. |
| `vspace`   | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es de lectura y escritura. |
| `width`    | Devuelve el valor del atributo del mismo nombre en el tag `<img>`. Es de lectura y escritura. |

Se puede descargar imágenes antes de su utilización para así en el momento que lo necesitemos, la página no necesite ir al servidor a descargar la imagen:

~~~javascript
var sustitucion = new Image(300, 197);
sustitucion.src = "imagenes/espacio.png";
~~~

## Botones 

| Propiedad | Actúa sobre                                     |
| --------- | ----------------------------------------------- |
| `value`   | Modifica la propiedad value de la etiqueta HTML |

`Id.bgColor = “#ff0000”` cambia el color de fondo a una tabla. 

Se pude pasar el id de la tabla pasando el objeto this:

~~~javascript
<td onMouseOver=“color(this);”>texto</td>
~~~

`Id.style.borderColor` modifica el color del borde. 

`Id.rows(num)` saber si existe esa fila. (Ver veracidad) 

`Id.delete.row(num)` elimina la fila. 

## Otros 

| Propiedad           | Se refiere a                                                 |
| ------------------- | ------------------------------------------------------------ |
| `element.innerHTML` | Devuelve o establece la sintaxis HTML describiendo los descendientes del elemento. |

 