# Ajax

AJAX (Asynchronous JavaSctipt And XML no es un lenguaje de programación, el navegador crea un objeto `XMLHttpRequest` para solicitar información a un servidor y esa información se puede utiliza con DOM. 

Para crear un objeto `XMLHttpRequest` se usa: 

~~~javascript
var xhttp = new XMLHttpRequest();
~~~


| Método                                | Descripción                                                  |
| ------------------------------------- | ------------------------------------------------------------ |
| `new XMLHttpRequest()`                | Crea un objeto.                                              |
| `abort()`                             | Cancela la solicitud actual.                                 |
| `getAllResponseHeaders()`             | Regresa la información del encabezado.                       |
| `getResponseHeaders()`                | Regresa información especifica del encabezado.               |
| `open(method, url, async, user, psw)` | Especifica una consulta. `method` tipo de consulta, `url` dirección del archivo, `async` sincronía, `user` usuario opciónal, `psw` contraseña opcional. |
| `send()`                              | Envía una petición al servidor, usada para respuesta tipo `GET`. |
| `send(string)`                        | Envía una petición al servidor, usada para respuesta tipo `POST`. |
| `setRequestHeader()`                  | Añade un par de etiqutas/valores al encabezado que se enviará. |

## Propiedades del objeto XMLHttpRequest. 

| Propiedad            | Descripción                                                  |
| -------------------- | ------------------------------------------------------------ |
| `onreadystatechange` | Define una función para ser llamada cuando la propiedad readyState cambie. |
| `readyState`         | Devuelve el estado de `XMLHttpRequest`. `0` consulta no iniciada, `1` conexión con el servidor establecida, `2` consulta recibida, `3` procesando consulta, `4` consulta terminada y la respuesta está lista. |
| `responseText`       | Regresa la información de repuesta como un string.           |
| `reponseXML`         | Regresa la información de respuesta como XML.                |
| `status`             | Regresa el número de estado de la solicitud. `200` "ok", `403` "prohibido", `404` "no funciona". |
| `statusText`         | Regresa un texto de estado.                                  |

## Código de ejemplo:

~~~php+HTML
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página</title>
        <script>
            function ajax(value){
                console.log(value);
                var xmlhttp = new XMLHttpRequest();
                xmlhttp.onreadystatechange = function(){
                    if(this.readyState == 4 && this.status == 200){
                        document.getElementById("text").innerHTML = this.responseText;
                    }
                };
                xmlhttp.open("GET", "request.php?q=" + value, true);
                xmlhttp.send();
            }
        </script>
    </head>
    <body>
        <form>
            <label>Texto: </label><input type="text" onkeyup="ajax(this.value);"><br>
        </form>
        <p id="text"></p>
    </body>
</html>
<?php
if($_SERVER["REQUEST_METHOD"] == "GET"){
    echo $_REQUEST["q"];
}
?>
~~~