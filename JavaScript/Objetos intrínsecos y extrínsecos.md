# Objetos intrínsecos y extrínsecos

## Intrínsecos 

`screen.width` anchura del monitor. 

`screen.height` altura del monitor. 

`screen.availwidth` anchura del área disponible. 

`screen.availheight` altura del área disponible. 

`screen.colordepth` profundidad de color. 

`screen.pixeldepth` profundidad de pixel. 

`window.open(URL)` abre otra ventana, en la URL especificada. nos regresa el valor de la ventana, en caso de no ser abierta nos regresa null. 

`window.close()` cierra la ventana. 

`window.moveTo()` mueve la ventana. 

`window.resizeTo()` cambia el tamaño de la ventana. 

`settimeout("función", retardo)` ejecuta una función cuando el contador finalice en milisegundos. nos regresa una variable con el contador. 

`cleartimeout(variable)` recibe como argumento una variable de un contador y la limpia. 

`setinterval("función", retardo)` ejecuta una función un número infinito de veces el con un lapso del tiempo establecido. nos regresa una variable con el intervalo. 

`clearinterval(variable)` recibe una variable de intervalo y lo limpia. 

`navigator.appname` nombre del navegador. 

`navigator.appversion` versión del navegador y el sistema operativo. 

`navigator.useragent` nos regresa varios datos sobre el navegador. 

`navigator.cookieenabled` si el navegador del cliente admite cookies. 

`navigator.language` idioma en el que está configurado el navegador. 

`navigator.online` nos dice si el navegador está conectado a internet. 

`navigator.plugins` nos regresa los plugin instalados en el navegador. 

`location.href` ubicación de la página web. 

`location.search` se emplea para búsqueda de archivos. identifica lo que aparece detrás del signo ? en una URL. 

`location.protocol`, `location.hostname`, `location.port`, `location.hash` 

`location.reload(variable)` recarga la página, si la variable es false se recarga desde la cache, si es true se recarga desde el servidor. 

`location.replace("URL")` remplaza la página que se va a cargar por una más apropiada, solo funciona cuando la página está cargando. 

`history.back()` retrocede una página. 

`history.foward()` avanza una página. 

## Extrínsecos 

Para crear tu propio objeto de JavaScript se hace como si fuera una función, esta funciona como el constructor de la función, donde los argumentos que le pongamos serán los que se utilicen. Para agregar sus atributos utilizamos la palabra reservada `this.el_nombre_del_atributo`. Por ejemplo: 

~~~javascript
function figura(num_lados){
    this.lados = num_lados
}
~~~

Para agregar métodos al objetos primero debemos crear una función que haga lo que queremos que haga el objeto, haciendo referencia a los atributos con la palabra reservada `this.nombre_del_atributo`, después con la propiedad `nombre_del_objeto.prototype.nombre_del_metodo` lo igualamos a la función que acabamos de crear. Por ejemplo: 

~~~javascript
function area(){
    return this.base * this.altura;
}
square.prototype.area = area(); 
~~~

 