# Animaciones

Para crear una animación debemos la regla `@keyframes`, la animación ira cambiando lentamente de un estilo a otro. 

Dentro del elemento se utilizan las siguientes propiedades: 

- `animation-name:` nombre del `@keyframe` a utilizar. 
- `animation-duration:` duración de la animación en segundos. 
- `animation-delay:` retraso para iniciar la animación, si tiene un valor negativo la animación iniciara como si hubiera pasado ese tiempo. 
- `animation-iteration-count:` número de veces que repetir la animación. 
  - `infinite`
- `animation-direction:` especifica como una animación debe de ser reproducida. 
  - `normal`
  - `reverse`
  - `alternate`
  - `alternate-reverse` 
- `animation-timing-function:` especifica la curva de velocidad de la animación. 
  - `linear`
  - `easev
  - `ease-in`
  - `ease-out`
  - `ease-in-out`
- `animation-fill-mode:` especifica un estilo para el elemento de destino cuando la animación no se ejecuta. 
  - `none`
  - `fowards:` el elemento conservará los valores de estilo que se define por el último fotograma clave. 
  - `backwards:` el elemento obtendrá los valores de estilo que se define por el primer fotograma clave, y retener a esto durante el periodo de retardo de animación. 
  - `both:` la animación seguirá las reglas de adelante y detrás, extendiendo las propiedades de animación en ambas direcciones. 

Dentro de `@keyframe` se utilizan las siguiente opciones: 

- `{ }` dentro de los corchetes se especifican que propiedades se cambiaran. 
- `from - to:` el estilo va a cambiar de 0% a 100% sin especificar un porcentaje. 
- `%` que propiedades van a cambiar cuando la animación llegue a ese porcentaje respecto al tiempo. 

