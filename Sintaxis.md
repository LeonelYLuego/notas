# Sintaxis de markdown

## Encabezados
# Título h1
## Título h2
### Título h3
#### Título h4
##### Título h5
###### Título h6

Este sería un encabezado subrayado
---
Este sería otro encabezado subrayado
===

## Citas

> Este sería una cita

> Este sería un bloque de citas
> 
> Una cita
> 
> Otra cita

> Una cita
>
> > Este es un bloque de cita dentro de otro bloque
> > 
> > Otra cita

## Listas

- Primer elemento
- Segundo elemento
* Tercer elemento
* Cuarto elemento
+ Quinto elemento
+ Sexto elemento

* Primer elemento
* Segundo elemento
	* Primer elemento
	* Segundo elemento
		* Tercer elemento
		* Cuarto elemento

1. Primer elemento
2. Segundo elemento
	1. Primer elemento
	2. Segundo elemento

## Código de bloque

~~~
#inlcude <iostream>
using namespace std;

int main(){
	cout << "Hola mundo" << endl;
	return 0;
}
~~~

## Regla horizontal

***

---

___

## Elemento de línea

*Cursiva* _Cursiva_

**Negrita** __Negrita__

***Cursiva negrita*** ___Cursiva negrita___

## Enlaces

[Enlace a una página web](http://www.google.com)

## Código

Una línea de código `#include` se escribe.

~~~javascript
//Este es un código javascript
function sum(num1, num2){
    return num1 + num2;
}
~~~

~~~c++
//Este es un código C++
double sum(double num1, double num2){
    return num1 + num2;
}
~~~

~~~python
#Este es un código en python
def sum(num1, num2):
    return num1 + num2
~~~



## Imágenes

![Texto alternativo](https://i1.wp.com/hotbook.com.mx/wp-content/uploads/2019/04/hotbook-se-revela-la-primera-imagen-de-un-agujero-negro-portada.jpg?w=1024&ssl=1 "Título alternativo")

## \

Los carácteres especiales no tienen efecto con \

\`Hola\`