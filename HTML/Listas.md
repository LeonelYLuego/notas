# Listas

Las listas es una manera elegante de mostrar los datos al usuario, existen las listas ordenadas, no ordenadas y de definiciones. Estás se pueden anidar entre si.

## Lista no ordenada

Los elementos `<li></li>` están dentro de las etiquetas `<ul></ul>`.

#### Ejemplo:

~~~html
<ul>  #Encierra todo el código de la lista
	<li>Blog</li> #Un elemento de la lista
</ul>
~~~

## Lista ordenada

Los elementos `<li></li>` están dentro de las etiquetas `<ol></ol>`.

### Atributos

- `type=""` especifica el marcador de la lista. 
  - 1 
  - A 
  - a 
  - I 
  - i 
- `start=""` indica en qué número o letra comenzar. 

#### Ejemplo:

~~~html
<ol>  #Encierra todo el código de la lista 
	<li>Titulo</li> #Un elemento de la lista que empieza por el valor 1 
</ol> 
~~~

## Lista de definición
Las definiciones están dentro de las etiquetas `<dl></dl>`, donde la palabra a definir se coloca entre las etiquetas `<dt></dt>` y su definición entre `<dd></dd>`.

#### Ejemplo:

~~~html
<dl>  #Encierra todo el código de la lista 
    <dt>Ordenador</dt> #Nombre que se va a definir 
    <dd>Es una máquina...</dd> #Definición 
</dl> 
~~~