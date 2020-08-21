# Funciones, objetos, matrices, cadenas, números y letras

## Funciones 

Una función se crea:

~~~javascript
function name(argumentos){
    //cuerpo de la función
    return value; //valor que regresa la función.
}

name(argumentos); //llamada a la función.
~~~

Es posible crear una función dentro de otra función. Existe una función llamada `eval('instrucción');` que ejecuta el código pasado como argumento. 

Las funciones cortas se declaran: 

~~~javascript
hello = () => {
    return "Hello World!";
}
~~~

Donde en los paréntesis van los parámetros de la función. 

Los argumentos de una función también pueden ser accedidos desde la variable `arguments` que es un array con todos los elementos. 

## Objetos

Los objetos pueden tener diferentes valores, para declarar uno:

~~~javascript
var car = {type:"Fiat", model="500", color:"white"};
~~~

Para acceder a un atributo del objeto ponemos el nombre del objeto seguido de un punto y el nombre del atributo al que queremos acceder.

Se pueden agregar métodos:

~~~javascript
var person = {
    name:"Juan",
    lastName:"Sanchez",
    fullName:function(){
        return this.name + " " + this.lastName;
    },
}; 
~~~

La palabra reservada `this` hace referencia a los atributos y métodos del mismo objeto. 

Para eliminar un elemento se utiliza `delete` seguido del `objeto.elemento`. 

## Matrices

En las matrices se pueden guardar datos de distinto tipo. 

Una matriz se declara: 

~~~javascript
var nombre = new Array("primer elemento", "segundo elemento");
var nombre = ["primer elemento", "segundo elemento"];

nombre[0]; //Acceder a los datos de una matiz
~~~

Se puede crear un Array con n elementos: 

~~~javascript
var points = new Array(40);
~~~

### Operaciones con matrices

`Array.isArray(array)` regresa verdadero si es un Array. 

`.toString()` convierte un array en String. 

`.indexOf(valor, inicio)` regresa la posición del valor. 

`.lenght` obtiene el número de elementos de la matriz. 

`.concat(matiz)` concatena dos matrices, agregando después de la primera, la segunda. 

`.join(cadena)` permite unir todos los elemento de una matriz en una cadena alfanumérica, separados por la cadena. 

`.pop()` se usa para eliminar el último elemento de la matriz. 

`.push(valor)` se usa para agregar un último elemento a la matriz. 

`.reverse()` permite invertir el orden en el que se encuentran almacenados los elementos en una matriz. 

`.shift()` se usa para eliminar el primer elemento de la matriz. 

`.unshift(valor)` permite insertar uno o más elementos al principio de la matriz. 

`.slice(inicio, fin)` crea una nueva matriz desde el elemento inicio hasta el fin. 

`.splice(inicio, número de celdas a eliminar, valor nuevo 1, valor nuevo n)`

`.sort()` ordena los datos de la matiz. 

Para agregar un nuevo método a las matrices:

~~~javascript
function suma{
    var sum = 0, cuenta;
    for(cuenta = 0; cuenta <= this.lenght; cuenta++){
        sum += this[cuenta];
    }
    return suma;
}
array.prototype.totalizar = suma;
var edades = new array(27, 20);
var total = edades.totalizar();
~~~

#### Iteraciones de una matriz 

Las iteraciones de una matriz son métodos que llaman a diferentes funciones, las funciones deben de tener como argumentos `function name(value, index, array)` 

`.forEach(función)` `for` que recorre todos los valores en la función. 

`.map(función)` `for` que recorre todos los valores en la función y regresa un nuevo array con valores retornados en la función. 

`.filter(función)` `for` que recorre todos los valores en la función y regresa un nuevo array con valores que cumplieron la expresión de retorno. 

`.reduce(función)` `for` que recorre todos los valores en la función y regresa un nuevo valor resultado de todas las iteraciones, es necesario agregar una variable al principio de los argumentos de la función que será la que recorrerá todas las iteraciones. 

`.reduceRight(función)` lo mismo que .reduce(función) pero en sentido contrario. 

`.every(función)` `for` que recorre todos los valores en la función y regresa un valor indicando si todos los valores de la matriz cumplieron con la condición de retorno. 

`.some(función)` `for` que recorre todos los valores en la función y regresa un valor indicando si alguno de los valores de la matriz cumplieron con la condición de retorno. 

`.find(función)` `for` que recorre todos los valores en la función hasta que encuentra un valor que cumple con la condición del `return` y lo regresa. 

`.findIndex(función)` lo mismo que `.find()` pero regresa la posición y no el valor. 

## Cadenas 

Una cadena se declara:

~~~javascript
var miCadena = new String(valor_literal);
~~~

Cadena de 3 digitos:

~~~javascript
var a = /\d\d\d/;
~~~

### Operaciones con cadenas

`.length` obtiene el número de caracteres de la cadena. 

`.link(referencia)` crea un nuevo vinculo hacía una página. 

`.big()` hace el texto más grande. 

`.blink()` hace que le texto parpadee. 

`.bold()` pone el texto en negritas. 

`.fixed()` pone el texto con ancho fijo 

`.fontcolor("#ffffff")` cambia el color. 

`.fontsize(9)` cambia el tamaño de letra. 

`.italics()` pone la letra en formato itálica. 

`.small()` pone la letra pequeña. 

`.strike()` pone la letra tachada. 

`.sub()` pone la letra como subíndice. 

`.sup()` pone la letra como superíndice. 

`.indexOf(cadena, inicio)` busca el primer índice que coincida con la cadena. Regresa -1 cuando no lo encuentra. El argumento inicio indica el índice en que comenzará a buscar. 

`.lastIndexOf(cadena)` busca el último índice que coincida con la cadena. 

`.charAt(índice)` regresa el carácter en la posición. 

`.charCodeAt(índice)` regresa el valor del carácter en la posición. 

`.slice(inicio, fin)` extrae una subcadena. 

`.split(carácter, inicio)` extrae diferentes subcadenas, separadas por el carácter denominado separador. 

`.substr(inicio, longitud)` extra una subcadena desde el inicio hasta la longitud dada. 

`.toUpperCase()` pone una cadena en mayúsculas. 

`.toLowerCase()` pone una cadena en minúsculas. 

`.concat(cadena)` concatena la primera cadena con la segunda. 

`.match(cadena)` regresa todas las subcadenas que coincidan con la cadena. 

`.search(cadena)` busca una cadena en la cadena, si la encuentra regresa su posición, sino, regresa -1. 

`.replace(cadena, remplazo)` busca la cadena en la cadena y la remplaza con en remplazo. 

`escape(cadena)` Convierte una cadena de texto normal en una cadena que pueda ser manejada por JavaScript. 

`unescape(cadena)` Convierte una cadena que puede ser manejada por JavaScript a una cadena de texto normal. 

`.trim()` remueve los espacios de una cadena.

### Caracteres especiales

| Secuencia de escape | Resultado                   |
| ------------------- | --------------------------- |
| `\b`                | Retroceso                   |
| `\f`                | Alimentación de formularios |
| `\n`                | Salto de línea              |
| `\r`                | Retorno de carro            |
| `\t`                | Tabulador horizontal        |
| `\v`                | Tabulador vertical          |

## Números 

`123e5`, `123e-5` número escrito de forma científica. 

`0.1`, `0.2` número flotante. 

`0xFF` número escrito en hexadecimal. 

`Number(value)` convierte el valor a número. 

`.toString()` convierte un número a String. 

`.toExponential()` regresa un String escrito de forma científica. 

`.toFixed()` regresa un String con un número flotante. 

`.toPrecision(n)` regresa un String con los n valores después del punto. 

`Number.NaN` un valor no numérico. 

`Infinity`, `-Infinity` un valor infinito. 

`isNaN(número)` regresa verdadero en caso de que el número sea nulo. 

## Objeto Math 

`Math.E` constante de euler 

`Math.LN2` ln(2) 

`Math.LN10` ln(10) 

`Math.LOG2E` log2( e ) 

`Math.LOG10E` log10( e ) 

`Math.PI` pi 

`Math.SQRT1_2` raíz cuadrada de 0.5. 

`Math.SQRT2` raíz cuadrada de 2. 

`Math.abs(n)` valor absoluto. 

`Math.acos(n)` arco seno. 

`Math.asin(n)` arco seno. 

`Math.atan(n)` arco tangente. 

`Math.atan2(x,y)` arco tangente de un punto determinado por las cordenadas. 

`Math.ceil(n)` redondeo de n al entero superior. 

`Math.cos(n)` coseno. 

`Math.exp(n)` e elevado a la n. 

`Math.floor(n)` redondeo de n al entero inferior. 

`Math.max(n,m)` el mayor de los dos. 

`Math.min(n,m)` el menor de los dos. 

`Math.pow(n,m)` el número n elevado a la m. 

`Math.random()` número aleatorio entre 0 y 1. 

`Math.round(n)` El redondeo de n. Si la parte decimal es inferior a 0.5, se redondea al inmediato inferior, si no, al inmediato superior. 

`Math.sin(n)` seno. 

`Math.sqrt(n)` raíz cuadrada de n. 

`Math.tan(n)` tangente. 

## Fecha 

Para declarar un objeto tipo fecha y obtener la fecha exacta de ese momento: 

~~~javascript
var fecha = new Date();
~~~

Si se quiere crear una fecha especifica, se debe crear con el constructor del objeto: 

~~~javascript
var fecha = new Date(año, mes, día, hora, minuto, segundo, milisegundo);
~~~

También se puede crear una fecha a partir de un String y milisegundos. 

### Operaciones con fechas

`.getFullYear()` el año completo, con cuatro cifras. 

`.getYear()` el año completo en un formato dependiente del navegador. 

`.getMonth()` el mes del año en número (de 0 a 11). 

`.getDate()` el día del mes, de 1 a 31. 

`.getDay()` el día de la semana en número(empieza en 0 con domingo). 

`.getHours()` la hora del día, de 0 a 23. 

`.getMinutes()` el minuto de la hora, de 0 a 59. 

`.getSeconds()` el segundo del minuto, de 0 a 59. 

`.getMiliseconds()` los milisegundos del segundo actual, de 0 a 999. 

`.getTime()` los milisegundos transcurridos desde el inicio de la era Unix. 

Los métodos `get`, también funcionan con `set`, para colocar un valor o con UTC. 

`.parse(cadena)` crea una marca de tiempo a partir de una cadena. 

`.toUTCString()` fecha mostrada de la manera estándar. 

`.toDateString()` fecha mostrada de la manera más leíble. 

### Formatos de fecha 

| Tipo        | Ejemplo                       |
| ----------- | ----------------------------- |
| ISO         | "2015-03-25T12:00:00-06:00"   |
| Fecha corta | "03/25/2015"                  |
| Fecha larga | "Mar 25 2015" o "25 Mar 2015" |