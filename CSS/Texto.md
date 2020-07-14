# Texto

`color:` define el color. 

`text-aling:` establece la alineación horizontal de un texto. 

- `left` alinear a la izquierda. 
- `right` alinear a la derecha. 
- `center` alinear al centro, centrar. 
- `justify` alinear a la izquierda y a la derecha, justificar. 

`text-decoration:` propiedad se utiliza para establecer o eliminar decoraciones de texto, se utiliza más para eliminar subrayado de enlaces. 

- `none` no produce ninguna decoración del texto. 
- `underline` el texto es subrayado. 
- `overline` el texto tiene una línea encima. 
- `line-through` el texto tiene una línea por el medo(tachado) 
- `blink` el texto parpadea. 

`text-transform:` se utiliza para especificar letras mayúsculas y minúsculas en un texto. 

- `capitalize` pone el primer carácter de cada palabra en mayúscula. 
- `uppercase` pone todos los caracteres de cada palabra en mayúsculas. 
- `lowercase` pone todos los caracteres de cada palabra en minúsculas. 
- `none` ningún efecto de cambio entre mayúsculas y minúsculas. 

`text-indent:` propiedad que se utiliza para especificar la sangría de la primera línea de un texto, consiste en empezar un renglón de un bloque de texto más adentro que el resto. Toma un valor de medida. 

`letter-spacing:` especifica el espacio entre los caracteres de un texto. 

`line-height:` especifica el espacio entre líneas, define la altura de cada elemento a nivel de línea. 

`direction:` cambia la dirección de un texto. 

`word-spacing:` especifica el espacio entre las palabras de un texto. 

`text-shadow:` establece una sombra a un texto, para generarlo, se puede visitar [www.css3gen.com/text-shadow/](http://www.css3gen.com/text-shadow/). 

`text-aling-last:` define la alineación de la última línea de un bloque de texto como un párrafo. 

`white-space:` indica como tratar los espacios en blanco dentro de un elemento. 

- `normal` los saltos de línea se indican con la etiqueta <br> y las líneas se cortan automáticamente para ajustar el ancho disponible. 
- `pre` los saltos de línea se producen por los saltos de línea que contenga el texto y las líneas no se cortan automáticamente. 
- `nowrap` similar al comportamiento normal, pero las líneas no se cortan automáticamente. 

`text-overflow:` especifica como el contenido desbordado debe mostrarse al usuario. 

- `clip` cortado 
- `ellipsis` puntos suspensivos. 

`word-wrap:` especifica si las palabras largas deben ser cortadas y puestas en el siguiente renglón. 

`word-break:` especifica si las palabras deben ser rotas por los espacios o por los caracteres. 

`writing-mode:` especifica si la línea debe posicionarse horizontalmente o verticalmente. 

## Fuente 

En CSS, hay dos tipo de nombres de la familia de fuentes: 

- Genérica de la familia: un grupo de familias de fuentes con un aspecto similar. 
- La fuente de la familia: un familia de fuentes específicas. 

`font-family:` especifica el tipo de letra. se separa por comas el orden que deberá de tomar el navegador las fuentes en caso de no encontrarlas. 

`font-style:` propiedad para especificar el texto en cursiva. 

- `normal`
- `italic`
- `oblique` 

`font-size:` establece el tamaño de letra. 

- absoluto 
  - px 
- relativo 
  - em (1 em es el tamaño de fuente actual, es igual a 16px) 
  - % 
  - vw ventana gráfica de anchura (1vw = 1 % del ancho de la ventana gráfica) 

`font-weight:` especifica el peso de un tipo de letra. 

- `normal` 
- `bold` 

`font-variant:` especifica si un texto debe ser representado en un pequeño-casquilla de fuente. (un pequeño-casquillo convierte todas las letras minúsculas a mayúsculas, sin embargo, las letras mayúsculas aparecen en un tamaño de letra más pequeño. 

Para agregar una fuente diferente se utiliza el código:

~~~css
@font-face{
	font-family: <un nombre de fuente remota>
	src: <origen> [, <origen>];
	[font-wight: <altura>;]
	[font-style: <estilo>; ]
}
~~~