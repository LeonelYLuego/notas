# Multimedia

## Imagen 

Se especifica con las etiquetas: `<img/>`.

- `src="imagen.jpg"` ubicación de la imagen 
- `alt="no se encontró la imagen"` descripción de la imagen 
- `width="800"` ancho de la imagen 
- `height="400"` alto de la imagen 
- `longdesc=""` URL sobre más información de la imagen 
- `usemap="#"` Id del mapa 

### Etiqueta `<picture>`

`<picture></picture>` Especifica los recursos de una imagen, la cambia según su tamaño o elige la primera imagen que sea compatible. 

- `<source></source>` Referencia a una fuente de imagen. 
  - `media="(min-width: 650px")` tamaño mínimo para utilizar esa imagen. 
  - `srcset="" url de la imagen` 
- `<img>` Último elemento, es utilizado por los navegadores que no soportan `<picture>` 

`<figure></figure>` utilizada como bloque donde pondremos alguna figura. 

- `<figcaption></figcaption>` descripción de la figura 

`<canvas></canvas>` reserva espacio en la página para algún recurso de javascript 

 

# Mapa de imagen 

Un mapa de imagen es una imagen con diferentes áreas para darle click, utiliza la etiqueta `<map></map>`. 

- `name=""` nombre del mapa. 

 

Para indicar las áreas donde están los puntos para hacer click se utiliza la etiqueta `<area>`. 

- `shape=""` indica la forma que se va a utilizar. 
  - rect rectángulo 
  - circle circulo 
  - poly región poligonal 
  - default toda la imagen 
- `coords=""` recibe las coordenadas de la figura, en el caso del círculo recibe la posición y el radio. 

 

# Vídeo 

Se especifica con las etiquetas: `<video></video>`.

- `autoplay` indica si la reproducción del video debe iniciar cuando sea posible. 
- `controls` especifica se los controles de reproducción, como los botones de inicio/paro o de avance/retroceso, se deben mostrar. 
- `height` indica la altura del reproductor del video. 
- `loop` indica si la reproducción del vídeo debe comenzar de forma automática cada vez que termine. 
- `muted` especifica que la salida del audio del vídeo debe de ser silenciada. 
- `poster` especifica una imagen que se muestra mientras el vídeo se descarga o hasta que el usuario pulse el botón de inicio. 
- `preload` indica se la carga del audio se debe de realizar antes de que sea necesaria se reproducción. 
- `src` indica la url del fichero del video. 
- `width` indica la anchura del reproductor del video. 
- `<source></source>` reproduce la primera pista de video con formato que reconozca. 
- `<track></track>` definir una pista de texto con información adicional. 
  - `default=""` pista por defecto que se debe emplear si el usuario no selecciona otra pista. 
  - `kind=""` tipo de pista, puede ser caption, chapters, descriptions, metadata y subtitles. 
  - `label=""` especifica el título de la pista. 
  - `src=""` url del fichero con la pista. 
  - `srclang=""` el idioma de la pista. 

 

# Audio 

Se especifica con las etiquetas `<audio></audio>`.

- `autoplay`: indica si la reproducción del audio debe comenzar en cuando sea posible. 
- `controls`: especifica si los controles de reproducción, como los botones de inicio/paro o de avance/retroceso, se deben mostrar. 
- `loop`: indica si la reproducción del audio debe comenzar de forma automática cada vez que termine. 
- `muted`: especifica que la salida del audio debe ser silenciada. 
- `preload`: indica si la carga del audio se debe realizar antes de que sea necesaria su reproducción. 
- `<source></source>` reproduce la primera pista de audio con formato que reconozca. 