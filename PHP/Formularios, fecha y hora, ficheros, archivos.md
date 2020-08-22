# Formularios, fecha y hora, ficheros, archivos

## Formularios 

Para obtener los datos enviados por un formulario se utilizan las variables  `$_GET`, `$_POST` que son arreglos que contienen los valores pasados por el formulario. Para mandar un formulario se recomiendo utilizar el nombre del archivo y a demás pasar los valores recibidos por una función que verifique la veracidad de ella. 

Para validar la entrada de datos por parte del usuario se puede consultar la página: https://www.w3schools.com/php/php_form_url_email.asp 

## Fecha y hora 

Las fechas se pueden obtener con la función `date("formato", [$variable])` donde el formato puede ir los siguientes caracteres: 

- `d` representa el día de la semana. 
- `m` representa el mes (1 a 12). 
- `M` representa el mes con letra. 
- `Y` representa el año en cuatro dígitos. 
- `l` representa el día de la semana. 
- `H` representa la hora (0 – 23). 
- `h` representa la hora (0 – 12). 
- `i` representa los minutos (0 – 59). 
- `s` representa los segundos (0 – 59). 
- `a` representa (am o pm). 
- `/`, `-`, `.`, `:` caracteres que se pueden utilizar para representar la fecha y hora. 

Para obtener la zona horaria se utiliza `date_default_timezone_set("America/Mexico_City");`

Se puede crear una variable de fecha y pasarla por `Date()` para obtener una fecha específica, para ello utilizamos la función `mktime(hour, minute, second, month, day, year);`

## Ficheros 

Se pueden incluir ficheros:

~~~php
include 'nombre_del_fichero';
require 'nombre_del_fichero';
~~~

La diferencia entre `include` y `require` es que si se busca un archivo y no es encontrado `include` va a proseguir con la ejecución del bloque, mientras que `require` no lo hará. En caso de que no encuentre el archivo se utiliza la sentencia `or die`.

## Archivos 

Para leer un archivo se utiliza la función `readfile("archivo");`, también existe la función `fopen("archivo", "modo");` donde por el modo se dice que se va a hacer con el archivo.

| Modo | Descripción                                                  |
| ---- | ------------------------------------------------------------ |
| `r`  | Abre un archivo para solo lectura.                           |
| `w`  | Abre un archivo para solo escritura, borra todo el contenido o crea un nuevo archivo si no existe. |
| `a`  | Abre un archivo para solo lectura, la información es preservada, el puntero inicia la final del archivo y crea uno nuevo si no es encontrado. |
| `x`  | Crea un nuevo archivo solo para escritura, regresa `false` y un error en caso de que ya exista uno. |
| `r+` | Abre un archivo de lectura escritura.                        |
| `w+` | Abre un archivo de lectura escritura, borra todo el contenido o crea un nuevo archivo si no existe. |
| `a+` | Abre un archivo de lectura escritura, la información es preservada, el puntero inicia al final del archivo y crea uno nuevo si no es encontrado. |
| `x+` | Crea un nuevo archivo de lectura escritura, regresa `false` y un error en caso de que ya exista uno. |

La función `fread($archivo, max_lenght)` lee un archivo abierto donde el segundo parámetros índica el máximo número de bytes para leer. 

Para cerrar un archivo se utiliza la función `fclose()`. 

Si se quiere leer una simple línea de un archivo se utiliza la función `fgets(archivo)` y si se quiere comprobar si se llegó al final de un archivo es dado por la función `feof(archivo)`, para leer un carácter es con la función `fgetc(archivo)`, por ejemplo: 

~~~php
while(!feof($myfile)){
	echo fgetc($myfile);
}
~~~

La función `fwrite(archivo, texto)` es utilizada para escribir un archivo. 

Para obtener más opciones sobre el archivo que se sube a un formulario se puede consultar en https://www.w3schools.com/php/php_file_upload.asp 