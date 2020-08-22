# POO

Una clase es como una función, pero dentro de ella existen más funciones y variables propias de la clase, además cuenta con un método llamado constructor. 

Para declarar una clase se utiliza la palabra reservada `class` y cada clase debe llevar consigo un constructor. 

~~~javascript
class Car{
    constructor(brand){
        this.carname = brand;
    }
}

mycar = new Car("Ford");
~~~
Para crear atributos dentro de una clase, se utiliza la palabra `this` seguida de un punto y el nombre del atributo con su valor. 

Los métodos son funciones que van dentro de la clase, para declarar un método primero se pone el nombre, seguido de los argumentos y entre corchetes el código a ejecutar. 

~~~javascript
class Car{
    present(){ return "I have a " + this.carname; }
}
~~~

Los métodos estáticos no necesitan un objeto, solo se pone el nombre de la clase seguido del método. Para declarar un método estático: 

~~~javascript
class Car{
    static hello() { return "Hello!"; }
}
~~~

## Herencia 

Una clase puede heredar los atributos y métodos de otra clase, para ello en la clase hija se declara: 

~~~javascript
class Model extends Car{
	...
}
~~~

Dentro del constructor de la clase hija se debe ejecutar el constructor de la clase padre, para ello se utiliza el método `super()` que hace referencia al constructor de la clase padre. 

## Get y Set 

Se pueden crear métodos que se escriban como atributos, estos pueden obtener un valor o retornarlo, para ello utilizan las palabras reservadas `set` y `get`, se utilizan de la siguiente manera: 

~~~javascript
class Car{
    get carname() { return this._carname; }
    set carname(x) { this._carname = x; }
}
~~~

 