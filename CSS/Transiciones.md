# Transiciones

La propiedad `transition:` permite cambiar los valores de una propiedad, desde un valor inicial a un valor final. Una transición se define con los siguientes parámetros: 

- `transition-property:` define la propiedad que va a experimentar la transición. Permite definir un conjunto de propiedades separadas por comas. 
- `transition-duration:` define la duración de la transición. 
- `transition-delay:` define el retraso de la transición entre el momento en que se activa el cambio de una propiedad y el inicio de la transición. 
- `transition-timing-fuction:` define la función de intervalo o de temporización de la transición que se emplea para calcular los valores intermedios entre el valor inicial y el valor final. 

Propiedades que pueden ser animadas 

| Propiedad             | Tipo de valor                     |
| --------------------- | --------------------------------- |
| `background-color`    | Color                             |
| `background-position` | Porcentaje \| longitud            |
| `border-color`        | Color                             |
| `border-width`        | Longitud                          |
| `border-spacing`      | Longitud                          |
| `bottom`              | Porcentaje \| longitud            |
| `clip`                | Rectángulo                        |
| `color`               | Color                             |
| `font-size`           | Longitud                          |
| `font-weight`         | Peso del tipo de letra            |
| `height`              | Porcentaje \| longitud \| cálculo |
| `left`                | Porcentaje \| longitud \| cálculo |
| `letter-spacing`      | Longitud                          |
| `line-height`         | Longitud \| número                |
| `margin`              | Longitud                          |
| `max-height`          | Porcentaje \| longitud \| cálculo |
| `max-width`           | Porcentaje \| longitud \| cálculo |
| `min-height`          | Porcentaje \| longitud \| cálculo |
| `min-width`           | Porcentaje \| longitud \| cálculo |
| `opacity`             | Número                            |
| `outline-color`       | Color                             |
| `outline-width`       | Longitud                          |
| `padding`             | Longitud                          |
| `right`               | Porcentaje \| longitud \| cálculo |
| `text-indent`         | Porcentaje \| longitud \| cálculo |
| `text-shadow`         | Una lista de sombras              |
| `top`                 | Porcentaje \| longitud \| cálculo |
| `vertical-align`      | Longitud                          |
| `visibility`          | Visibilidad                       |
| `width`               | Porcentaje \| longitud \| cálculo |
| `word-spacing`        | Longitud                          |
| `z-index`             | Entero                            |

 

Para hacer uso de las transiciones se puede utilizar la función de los selectores, por ejemplo: `hover`, que se activa cuando el cursor pasa sobre el él.

~~~css
div{
	transition: all 0.2s ease 0s;
}
div.hover{
	color: blue;
}
~~~

## Funciones de intervalos de transición 

La propiedad `transition-timing-fuction:` define la función de intervalo o de temporización de una transición. La función de intervalo determina el cálculo de los valores intermedios que toma una propiedad entre el valor inicial y el valor final. 

La función de intervalo se especifica mediante una curva definida con una función de Bézier de cuatro puntos. Alterando la posición de los cuatro puntos P0, P1, P2 y P3 se definen distintas curvas. 

![Resultado de imagen para curva de bezier para la funcion transición](data:image/png;base64,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)

 

La curva de Bézier se define con la función `cubic-bezier()`, que recibe 4 parámetros. Además, en su lugar de especificar una curva de Bézier, existen varias funciones predeterminadas: 

- `ease` define un inicio lento, después uno rápido y, por último, un final lento. 
- `linear` define una transición con la misma velocidad desde el inicio hasta el final. 
- `ease-in` define una transición con inicio lento. 
- `ease-out` define una transición con un final lento 
- `ease-in-out` define una transición con un inicio y un final lento. 

"CSS Esaing Animation Tool" es una herramienta en línea para calcular. 