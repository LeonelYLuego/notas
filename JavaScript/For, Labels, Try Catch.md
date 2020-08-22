# For, Labels, Try-Catch

## For 

`for/in` bucle con el mismo número de vueltas que elementos en un array, la variable es un iterador. 

~~~javascript
var person = {fname:"John", lname:"Doe", age:25};
var text = "";
var x;
for (x in person) {
    text += person[x];
}
~~~

`for/of` bucle donde la variable toma el valor de los elementos del array.

~~~javascript
var cars = ['BMW', 'Volvo', 'Mini'];
var x;
for (x of cars) {
    document.write(x + "<br >");
}
~~~

## Etiquetas 

Las etiquetas sirven para separar un código en un bloque, y cuando llegue a un break salir de la etiqueta.

~~~javascript
var cars = ["BMW", "Volvo", "Saab", "Ford"]; 

list: {
    text += cars[0] + "<br>";
    text += cars[1] + "<br>";
    break list;
    text += cars[2] + "<br>";
    text += cars[3] + "<br>";
}
~~~

## Try-Catch 

Para el manejo de errores se utilizan las sentencias `try-catch`, donde el argumento de `catch` debe ser el nombre de la variable, está guarda el error que sucedió, y para acceder a el sólo debemos imprimirlo. 

Se pueden crear error con la palabra reservada `throw` seguida de lo que queremos lanzar como error. 

`finally` ejecuta un código independientemente si ocurrió un error o no. 