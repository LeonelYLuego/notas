# Tipo de datos

`var_dump()` regresa el tipo de dato y el valor. 

Para castear entre los tipos de datos, se agrega antes del identificador y entre paréntesis el tipo de dato al cual se quiere convertir. 

## String 

Las cadenas de caracteres pueden llevar comillas simples o dobles: `'Hello'`, `"Hello"`.

| Función                               | Descripción                                                  |
| ------------------------------------- | ------------------------------------------------------------ |
| `strlen(string)`                      | Regresa la longitud del string.                              |
| `str_word_count(string)`              | Regresa el número de palabras que hay en un string.          |
| `strrev(string)`                      | Voltea un string.                                            |
| `strpos(string, string)`              | Regresa la posición donde busca el segundo string en el primero. |
| `str_replace(string, string, string)` | Remplaza el primer string con el segundo en la tercera cadena. |

## Enteros 

Los enteros pueden ir desde `-2,147,483,648` hasta `2,147,483,647`. 

| Función              | Descripción                                |
| -------------------- | ------------------------------------------ |
| `is_int(value)`      | Regresa verdadero si el valor es entero.   |
| `is_finite(value)`   | Regresa verdadero si el valor es finito.   |
| `is_infinite(value)` | Regresa verdadero si el valor es infinito. |
| `is_nan(value)`      | Regresa verdadero si el valor es nulo.     |

## Flotante 

Los flotantes se especifican con un número con punto decimal. 

| Función           | Descripción                                |
| ----------------- | ------------------------------------------ |
| `is_float(value)` | Regresa verdadero si el valor es flotante. |

## Booleano 

Varia entre un estado falso y uno verdadero. 

## Array 

Espacio de memoria que es utilizada para guardar más de un solo valor en una variable, se declara: 

~~~php
$cars = {"audi", "volvo"};
~~~

También se puede declarar: 

~~~php
$cars = array("audi", "volvo"); 
~~~

Los arrays asociativos son aquellos que como subíndice llevan una palabra clave, estos se declaran: 

~~~php
$age = array("Ben"=>"37", "María"=>"28");
~~~

estos se pueden meter en un foreach:

~~~php
foreach($age as $x => $y){
    
}
~~~

| Función    | Ordenamiento                        |
| ---------- | ----------------------------------- |
| `sort()`   | Ordenamiento ascendente.            |
| `rsort()`  | Ordenamiento descendente.           |
| `asort()`  | Ordenamiento ascendente por valor.  |
| `ksort()`  | Ordenamiento ascendente por llave.  |
| `arsort()` | Ordenamiento descendente por valor. |
| `krsort()` | Ordenamiento descendente por llave. |

## Objeto 

Estructura que guarda atributos y métodos. 

~~~php
class Car{
    function Car(){
        this->model = 'VW';
    }
}
$x = new Car();
~~~

Valor nulo 

Para expresar un valor nulo se utiliza la palabra reservada `null`. 