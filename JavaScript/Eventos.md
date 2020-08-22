# Eventos

Los eventos son acciones sobre la página web que hacen que sucedan cosas, estos van en los elementos del código HTML. Para agregar un evento: 

~~~html
<elemento evento="código JS"> 
~~~

Algunos de los eventos son:

| Evento         | Descripción                                                  |
| -------------- | ------------------------------------------------------------ |
| `onchange`     | Un elemento HTML ha sido cambiado.                           |
| `onclick`      | Ocurre cuando el botón del dispositivo apuntado es pulsado sobre un elemento. Se puede emplear en la mayoría de las etiquetas. |
| `onmouseover`  | Este evento ocurre cuando el dispositivo apuntador se mueve sobre un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. |
| `onmouseout`   | Este evento ocurre cuando el dispositivo apuntador es movido fuera de un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. |
| `onkeydown`    | Este evento ocurre cuando una tecla es presionada sobre un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. |
| `onload`       | Ocurre cuando finaliza la carga de una página en una ventana o de todos los marcos en una página dividida en marcos. Se puede emplear en `<body>`, `<frameset>`. |
| `onunload`     | Ocurre cuando se quita una página web de una ventana o de una marco. Se puede emplear en `<body>`, `<frameset>`. |
| `ondblclick`   | Ocurre cuando el botón del dispositivo apuntador es pulsado dos veces sobre un elemento. Se puede emplear en la mayoría de las etiquetas. |
| `onmousedown ` | Este evento ocurre cuando el botón del dispositivo apuntador es presionado sobre un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. Este evento es distinto de `onclick`, ya que este último se origina cuando se presiona y se suelta el botón. |
| `onmouseup`    | Este evento ocurre cuando el botón del dispositivo apuntado es soltado sobre un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. |
| `onmousemove ` | Este evento ocurre cuando el dispositivo apuntador se mueve mientras está sobre un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. |
| `onfocus`      | este evento ocurre cuando un elemento recibe el foco, ya sea por el dispositivo apuntador o mediante tabulación. Este atributo se puede emplear con las etiquetas `<a>`, `<area>`, `<label>`, `<input>`, `<select>`, `<textarea>`, `<button>`. |
| `onblur`       | Este evento ocurre cuando un elemento pierde el foco, ya sea por el dispositivo apuntador o mediante tabulación. Este atributo se puede emplear con las etiquetas `<a>`, `<area>`, `<label>`, `<input>`, `<select>`, `<textarea>`, `<button>`. |
| `onkeypress`   | Este evento ocurre cuando una tecla es presionada y soltada sobre un elemento. Este atributo se puede emplear con la mayoría de las etiquetas. |
| `onkeyup`      | Este evento ocurre cuando una tecla es soltada sobre un elemento. Este atributo se puede emplear en la mayoría de las etiquetas. |
| `onsubmit`     | Este evento ocurre cuando un formulario es enviado. Este atributo solo se puede emplear con la etiqueta `<form>`. |
| `onreset`      | Este evento ocurre cuando un formulario es borrado. Este atributo sólo se puede emplear con la etiqueta `<input>` y `<textarea>`. |
| `onchange`     | Este evento ocurre cuando un control pierde un foco de entrada y su valor ha sido modificado desde que obtuvo el foco. Este atributo se puede emplear con las etiquetas `<input>`, `<select>` y `<textarea>`. |

