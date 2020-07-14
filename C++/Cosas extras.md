# Cosas extras

### Variables

`wchar_t` variable para caracteres de 2 bytes. 

`long double` variable real más grande que la double. 

`typedef int entero;` sinónimo de tipo de variable.

`not_eq ` es lo mismo que `!=`.

`int t = sizeof a;` tamaño en bytes de la variable.

`sizeof(int)` tamaño en bytes del tipo de variable.

### Casteo

`static_cast<T>(v);` `reinterpret_cast<T>(v);` `dynamic_cast<T>(v);` `const_cast<T>(v);` Cast, conversion forbade.

### Directrices de preprocesado

`#include` incluir librerías.

`#define` define un identificador (ID significado).

`#ifndef` si no está definido.

`#if` si se cumple esta condición compila lo siguiente.

`#else` si no se cumple la condición compila lo siguiente.

`#elif` else if.

`#endif` terminal el if.

### Modificadores de variables

`static` variable que se inicia en 0 o en el valor que le damos y que al salir del bloque y regresar sigue teniendo su valor.

`extern` utilizar una variable cuando su definición esta abajo de ella, es global.

`auto` sólo es visible en el bloque donde está definida.

`register` que se pueden guardar para ocupar menos espacio en un registro del equipo.

### Entrada y salida estandar

`cin >> hex >> var` leer en hexadecimal la variable.

`cin >> dato >> dato2` sirve para obtener datos numéricos de los diferentes tipos.

`cin.get();` obtiene solo un carácter en ASCII.

`getline(cin, string);` puede obtener una línea de caracteres hasta \n para una cadena de caracteres.

`getline(cin, datos, ';');` obtiene datos y los guarda en un string hasta llegar al carácter dicho.

### Punteros y matrices

`void Funcion(m[]) {` pasar una matriz completa por una funcion.

`m = v;` donde se puede pasar un vector completo a otro.

`char cadena[10] = "abcd";` podemos agregar los valores de caracteres de esta manera y automáticamente el ultimo se pone '\0' para saber que es el final.

`int *q = static_cast<int *> (p);` conversion de un puntero a otro tipo por ejemplo void *. 

`const tipo *nombre-punt = ...;` puntero que se puede cambiar de direccion pero no puede cambiar el valor apuntado.

`tipo* const nombre-punt = ...;` puntero que no se puede cambiar de direccion pero puede cambiar el valor apuntado.

`const tipo* const nombre-punt = ...;` puntero  que no se puede cambiar de direccion ni puede cambiar el valor apuntado.

`int& ultimo = a[4];` se crea un un sinonimo al valor numerico.

`fill(p, p + nbytes, 0);` pone esa memoria desde el primer puntero al ultimo en el valor especificado.

### Enumeraciones y espacios de nombre

Función: tipo-resultado [ámbito::] nombre-función ([parámetros formales])  

~~~c++
enum colores {
	azul = 0, // azul representa el 0 y asi sucesibamente 
    amarillo,
    verde,
    rojo,
    cafe
};

colores = azul; 
~~~

~~~c++
namespace System {
	class a {};
	class b {};
	namespace Windows { 
		namespace Forms {
			class c {};
			class d {};
		}
	}
}  
System::Windows::Forms::c obj; 
~~~

