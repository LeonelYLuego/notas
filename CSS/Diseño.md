# Diseño

## Fondo 

`background:` propiedad abreviada de las siguientes. 

`background-color:` establece un color de fondo. 

`background-image:` establece una imagen como fondo, se pueden agregar más de una separándolas con comas, donde la primera imagen es la más cercana al espectador. 

- `url("")` 
- `linear-gradient(dirección, color1, color2)` gradiente lineal, `repeating-linear-gridient` gradiente lineal repetido.
  - `to rigth bottom`
  - `90deg ángulo`
  - `15% espacio del color`
- `radial-gradient` gradiente radial, `repeating-radial-gradient` gradiente radial repetido. 
  - `circle`
  - `ellipse`
  - `closest-side`
  - `farthest-side`
  - `closest-corner`
  - `farthest-corner`

`background-repeat:` establece si se repite el fondo de imagen. 

- `repeat-x` lo repite en el eje de las x. 
- `repeat-y` lo repite en el eje de las y. 
- `no-repeat` no lo repite. 

`background-size:` tamaño del fondo de la imagen. 

- `cover` llena todo el elemento. 
- `contain` escala la imagen tan grande como sea posible, puede dejar espacios en blanco. 

`background-position:` indica la posición de una imagen de fondo. 

`background-attachment:` indica si la imagen debe desplazarse o quedarse estática. 

- `fixed` fijo 
- `scroll` moverse con la página 

`background-clip:` especifica el área de pintura del fondo. 

- `border-box` el fondo está pintado hasta el borde exterior del borde. 
- `padding-box` el fondo está pintado hasta el borde exterior del relleno. 
- `content-box` el fondo está pintado hasta el cuadro del contenido. 

`background-origin:` especifíca donde se ubica las imágenes de fondo. 

- `border-box` la imagen de fondo se inicia desde la esquina superior izquierda del borde. 
- `padding-box` la imagen de fondo se inicia desde la esquina superior izquierda del relleno. 
- `content-box` la imagen de fondo se inicia desde la esquina superior izquierda del contenido. 

## Opacidad y transparencia 

`opacity:` especifica la opacidad y transparencia de un elemento, puede tomar valores desde 0 a 1. 

## Sombras 

Las sombras se pueden agregar con las propiedades `text-shadow` y `box-shadow`, estas tiene 4 valores: 

- distancia en horizontal. 
- distancia en vertical. 
- blur (desenfoque) en px. 
- color. 

Se pueden agregar múltiples sombras separadas por una coma, también se puede generar con la propiedad un borde alrededor del textos. 

## Estilos de diseño 

Diseño fijo: la anchura del contenido de la página y de los diferentes componentes de la página se especifican con unidades de medidas absolutas, normalmente píxel. 

Diseño líquido: la anchura de los componentes de la página se especifica mediante porcentajes respecto a la anchura de la ventana del navegador. 

Diseño elástico: la anchura de los componentes de la página se especifica en unidades relativas respecto al tamaño del texto. 

Diseño adaptativo: se basa en el empleo de media query. La condición se basa en características del medio en el que se muestra la página web, como el ancho o el alto del dispositivo de visualización. Una media query emplea la regla @media de CSS junto con una condición que evalúa alguna característica del dispositivo: `width`, `height`, `orietation`, `color`.

### Ejemplo 

~~~css
@media screen and (max-width: 800px){
    card{
        width: 300px;
    }
}
~~~