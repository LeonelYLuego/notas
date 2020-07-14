# POO

Para crear una clase en PHP se utiliza la palabra reservada `class`, para crear los atributos de la clase se pone el modificador de acceso seguido del nombre de la variable, y para agregar los métodos de la clase se utiliza la palabra reservada `function` seguido de su identificador y los parámetros del método. 

~~~php
class Fruit{
    public $color;
    function set_color($new){ $this->name = $new; }
}
~~~

Para crear un objeto se hace como a continuación: 

~~~php
$banana = new $Fruit;
$banana->set_color("Yellow");
~~~

Se puede comprobar si el objeto es de la clase especificada con: 

~~~php
var_dump($banana instanceof Fruit);
~~~

 Para utilizar el constructor de la clase se utiliza function `__construct(parametros)` y para el destructor del objeto se utiliza function `__destruct(parametros)`. 

Los modificadores de acceso son: 

- `public` puede ser accedido desde cualquier lado (por defecto). 
- `protected` la propiedad puede ser accedida por la clase y por las clases heredadas. 
- `private` solo puede ser accedido por la clase. 

Para heredar una clase se utiliza la palabra reservada `extends`, por ejemplo: 

~~~php
class Strawberry extends Fruit{

}
~~~

El constructor de una clase heredada no llama al constructor de se clase padre, si no todo se inicia desde el constructor de la clase heredada. 

La palabra `final` evita que la clase puede tener herencia. 

~~~php
final class Fruit{
    
}
~~~

Se pueden crear atributos constantes, estos se declara por ejemplo: 

~~~php
const MESSAGE = "Bye";
~~~

Para utilizar un atributo constante fuera de la clase se utiliza el nombre de la clase seguido de `::` y el nombre del atributo. Para utilizarlo dentro de la clase se utiliza `self::` y el nombre del atributo. 

Los métodos abstractos son métodos que son declarados en la clase padre pero son definidos solo por las clases hijas. Para declarar una método abstracto:

~~~php
abstract public function someMethod1() : string;
~~~

Después de los dos puntos va el tipo de valor que podría regresar.

Es posible tener métodos que pueden ser agregados a una clase sin la necesidad de una herencia, para ello se meten en el bloque de `trait`: 

~~~php
trait TraitNmae{
	public function msg1(){}
}
~~~

Para usarlos, dentro de la clase se utiliza la palabra reservada `use` seguido del nombre del bloque `trait`.  

Los métodos y atributos estáticos son métodos y atributos que no necesitan instanciar un objeto para poderlos utilizar, solo es necesario el nombre de la clase. 

~~~php
public static function welcome(){

}
public static $color;
greeting::welcome();
greeting::$color;
~~~