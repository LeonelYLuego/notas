# Transformaciones

Para utilizar las transformaciones, utilizamos la propiedad `transform:` 

- `scale():` permite modificar el tamaño del elemento. Esta función recibe dos parámetros: el valor X para el eje horizontal y el valor Y para el eje vertical. Los valores van entre 0 y 1. 
  - `scaleX():`
  - `scaleY():`
- `rotate():` rota o gira un elemento el número de grados indicados en le sentido de las agujas de reloj. 
  - `rotateX():`
  - `rotateY():`
  - `rotateZ():`
- `skew():` permite inclinar un elemento y cambiar la simetría del eje horizontal y vertical. Esta función recibe dos parámetros: el primero para el eje horizontal y el segundo para el eje vertical. 
  - `skewX():`
  - `skewY()`
- `translate():` traslada un elemento de posición. Esta función recibe dos parámetros, el primero para la translación en el eje horizontal y el segundo para la translación en el eje vertical. 
  - `translateX()`
  - `translateY()`
- `matrix(scaleX(), scaleY(), skewX(), skewY(), translateX(), translateY()):` junta todas las transformaciones. 